import os, re, subprocess, shutil, platform, string
import xml.etree.ElementTree as ElementTree

from ide import Ide, TestError
from subprocess import check_output

class SW4STM32_W(Ide):
	"""
		The SW4STM32 class is derived from the Ide abstract class and 
		provides support for the System Workbench IDE.
	"""
	_executable=[]
	_Folder='SW4STM32'
	_Extension='.cproject'
	_SW4_workspace='.__workspace'
	_environ=""
	_makedir=""
	_compdir=""
	
	def __init__(self):
       
		sw     = []

		for drive in string.ascii_lowercase:

			searchpath ="C:/Ac6/SystemWorkbench/"
			if os.path.isdir(searchpath):
				execs   = self.findPattern( 'eclipsec.exe', searchpath )
				sw4dir   = searchpath + '/plugins'
				make     = self.findList('make.exe', sw4dir)
				compiler = self.findList('arm-none-eabi-gcc.exe', sw4dir)
				
				if ( len(execs) > 0 )  & ( len(make) > 0 ) & ( len(compiler) > 0 ) :
					makedir=os.path.dirname(make[len(make)-1])
					makedir_msys=makedir.replace('\\', '/')
					makedir_msys=makedir_msys.replace(drive + ':', '/' + drive)
					compdir=os.path.dirname(compiler[len(compiler)-1])
					compdir_msys=compdir.replace('\\', '/')
					compdir_msys=compdir.replace('c:', '/c')
					environ=makedir_msys + ':' + compdir_msys
					
					sw.append( {"exec":execs[0], "makedir":makedir, "compdir":compdir, "environ":environ })
		
		if len(sw) == 0: raise TestError()
		
		# choose the latest
		choice = len(sw) - 1
		
		self._executable = sw[choice]["exec"]
		self._makedir    = sw[choice]["makedir"]
		self._compdir    = sw[choice]["compdir"]
		self._environ    = sw[choice]["environ"]
	
	def compile(self, path, type, board, name, target, output):
		"""
			compile the given projct and returns the generated binary
			
			compile function calls the IDE to compile the project, raising an
			error if the project fails (printing only number of found warnings)
			and returns a list of filenames of the created binaries
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be compiled
				output:		a filename where to store the output
			Returns:
				A list of dictionary entries, organized in this way
				entry={'ide':'IAR', 'project': name, 'folder': projectfolder, 'board':board, 'target':t, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex}
				ide:		name of the IDE that generated the entry
				project:	name of the project that generated the entry
				folder:     name of the top folder where the project is saved
				board: 		name of the Nucleo board for which the project was generated
				target:   	the name of the compiled target
				error:    	the error code, following this nomenclature
						-1: the program failed to start 
						 0: no error
						>0: some error occurred, exit code depending from the IDE, for Keil
								1: some warnings when compiling
								2: errors
				warning:  	number of warnings
				binaries: 	a list of compiled binaries		
		"""
		ret = []
		
		project=self.findProject(path, type, board, name)
		# project not found or not existing
		if len(project) == 0:
			return ret
		binstore=[]
		projectfolder=os.path.dirname(project)
		projectfolder=os.path.realpath(projectfolder)
		
		if os.path.isdir(self._SW4_workspace):
			shutil.rmtree(self._SW4_workspace)
			
		# this is for some problems of Eclipse when dealing with msysgit bash
		if os.environ.get('MAKE_MODE') == None:
			epath=''
		else:
			print('SORRY, won\'t work with msysgit shell')
		
		if target == "-ALL":
			cmdstring = "\"" + self._executable + "\"  --launcher.suppressErrors -nosplash -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + self._SW4_workspace + epath + " -import \"" + projectfolder + "\" -cleanBuild all"
		else:
			cmdstring = "\"" + self._executable + "\"  --launcher.suppressErrors -nosplash -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + self._SW4_workspace + epath + " -import \"" + projectfolder + "\" -cleanBuild " + name + "/" + target
			
		num_error = 0
		num_warn  = 0
		try: 
			print("--SW4  [ " + board + " ]: compiling " + name + ' for configuration ' + target )
			retval=check_output( cmdstring, shell=True )
			#print retval
		except subprocess.CalledProcessError as e:
			filename = output + ".txt"
			#print(" ERROR executing the command ")
			#print("       " + cmdstring )
			with open(filename, 'w') as f:
				f.write(str(e.output))
			num_error = -1

		if num_error == 0:
			retval=str(retval)
			num_warn=retval.count('warning')

		bin = self.findPattern('*.bin', projectfolder)
		hex = self.findPattern('*.hex', projectfolder)
		lib = self.findPattern('*.lib', projectfolder)
		a   = self.findPattern('*.a', projectfolder)
		if bin==[]:
			    print('\n')
			    print("binary not generted")
			    bin="empty"
			    print('\n')
		#print retval
		entry={'ide':'SW4STM32', 'project': name, 'folder': projectfolder, 'board':board, 'target':target, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex, 'lib':lib, 'a':a}
		ret.append(entry)
		print (" -----------IDE -SW4STM32------------------  ")
		print ("PROJECT NAME  : ",name)
		print ("BOARD : ",board)
		print('\n')
		print("Number of Errors" ,num_error )
		print("Number of Warnings" ,num_warn )
		binstore.append(board)
		#bin[0]="['"+bin[0]+"']"
		#print("binnnnnnnnnnnnn",bin[0])
		binstore.append(bin)
		dir=os.getcwd()
		self.binGeneration(dir,entry)
		return binstore
	def binGeneration(self, path, e):
		"""
			copy binaries .bin .hex in appropriate folder
			
			binGeneration() function copy the bin file to the appropriate Binary/
			folder and generates the corresponding .hex file through the 
			objcopy file
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				e:          the list of items that were returned from the compile phase
			Returns:
				a list of binaries generated in the compile phase
		"""
		projectfolder = e['folder']
		multi = path + '/Multi'
		if os.path.isdir(multi):
			binfolder     = projectfolder + "/../../../Binary/" + e['board'] + "/"
		else:
			binfolder     = projectfolder + "/Binary/"
		
		if not os.path.isdir(binfolder):
			os.makedirs(binfolder)

		target = e['target']
		list = []
		
		if len(e['bin']) > 0:
			if target == '-ALL':
				targetlist = e['bin']
			else:
				targetlist = [ target ]
			for bin in targetlist:
				target       = os.path.split(os.path.dirname(bin))[1]
				filename_bin =binfolder + e['board'] + ".bin"
				shutil.copy(bin, filename_bin)
				
				# generate the hex counterpart
				filename_hex = binfolder + e['board'] + ".hex"
				#implement tool for bin -> hex conversion
				# $objcopy -I binary $binary_file -O ihex $hex_file --change-addresses 0x08000000
				cmdstring = self._compdir + "/arm-none-eabi-objcopy.exe -I binary " + filename_bin + " -O ihex " + filename_hex + " --change-addresses 0x08000000"
				try:
					retval = check_output( cmdstring, shell=True )
				except subprocess.CalledProcessError:
					print(" ERROR executing the command ")
					print("       " + cmdstring )
				list.append(filename_bin)
				list.append(filename_hex)
					
		return list
				

	def clean(self, path, type, board, name, target):
		"""
			clean the given project 
			
			compile function calls the IDE to clean the project, 
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
		"""
		return 0
	
	
class SW4STM32_L(Ide):
	"""
		The SW4STM32 class is derived from the Ide abstract class and 
		provides support for the System Workbench IDE.
	"""
	_executable=[]
	_Folder='SW4STM32'
	_Extension='.cproject'
	_SW4_workspace='.__workspace'
	_environ=""
	_compdir=""
	
	def __init__(self):
		"""
		Initializes the environment
		
		__init__ setup the environment and raises an exception if it does
		not find what it is searching: the SystemWorkbench eclipsec executable,
		a make and arm-none-eabi-gcc binaries
		
		Args:
				self:  		self of the given object
		"""
		users=self.findImmediateSubdirectories('/home')
		if 'users' in users:
			users.remove('users')
			users2=self.findImmediateSubdirectories('/home/users')
			for user in users2:
				swdir= '/home/users/' + user + '/Ac6/SystemWorkbench'
				sw=self.findPattern('eclipse',swdir)
				if len(sw) > 0:
					sw=sw[0]
					self._executable=sw
					ac6home = swdir
		for user in users:
			swdir= '/home/' + user + '/Ac6/SystemWorkbench'
			sw=self.findPattern('eclipse',swdir)
			if len(sw) > 0:
				sw = sw[0]
				self._executable = sw
		
		if len(self._executable) == 0:
			raise TestError()
		
		compdir       = self.findPattern('arm-none-eabi-gcc', ac6home)
		
		if len(compdir) == 0:
			raise TestError()
			
		self._compdir       = os.path.dirname(compdir[len(compdir)-1])
		self._environ = self._compdir
	
	
	def compile(self, path, type, board, name, target, output):
		"""
			compile the given projct and returns the generated binary
			
			compile function calls the IDE to compile the project, raising an
			error if the project fails (printing only number of found warnings)
			and returns a list of filenames of the created binaries
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be compiled
				output:		a filename where to store the output
			Returns:
				A list of dictionary entries, organized in this way
				entry={'ide':'IAR', 'project': name, 'folder': projectfolder, 'board':board, 'target':t, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex}
				ide:		name of the IDE that generated the entry
				project:	name of the project that generated the entry
				folder:     name of the top folder where the project is saved
				board: 		name of the Nucleo board for which the project was generated
				target:   	the name of the compiled target
				error:    	the error code, following this nomenclature
						-1: the program failed to start 
						 0: no error
						>0: some error occurred, exit code depending from the IDE, for Keil
								1: some warnings when compiling
								2: errors
				warning:  	number of warnings
				binaries: 	a list of compiled binaries		
		"""
		ret = []
		project=self.findProject(path, type, board, name)
		# project not found or not existing
		if len(project) == 0:
			return ret
		
		projectfolder=os.path.dirname(project)
		projectfolder=os.path.realpath(projectfolder)
		
		if os.path.isdir(self._SW4_workspace):
			shutil.rmtree(self._SW4_workspace)
			
		# this is for some problems of Eclipse when dealing with msysgit bash
		if os.environ.get('MAKE_MODE') == None:
			epath=''
		else:
			print('SORRY, won\'t work with msysgit shell')
			
		
		if target == "-ALL":
			cmdstring = "\"" + self._executable + "\"  --launcher.suppressErrors -nosplash -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + self._SW4_workspace + epath + " -import " + projectfolder + " -cleanBuild all"
		else:
			cmdstring = "\"" + self._executable + "\"  --launcher.suppressErrors -nosplash -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + self._SW4_workspace + epath + " -import " + projectfolder + " -cleanBuild " + name + "/" + target
			
		num_error = 0
		num_warn  = 0
		try: 
			print("--SW4  [ " + board + " ]: compiling " + name + ' for configuration ' + target )
			retval=check_output( cmdstring, shell=True )
		except subprocess.CalledProcessError as e:
			filename = output + ".txt"
			print(" ERROR executing the command ")
			print("       " + cmdstring )
			with open(filename, 'w') as f:
				f.write(str(e.output))
			num_error = -1
		
		
		if num_error == 0:
			retval=str(retval)
			num_warn=retval.count('arning')
		
		bin = self.findPattern('*.bin', projectfolder)
		hex = self.findPattern('*.hex', projectfolder)
		lib = self.findPattern('*.lib', projectfolder)
		a   = self.findPattern('*.a',   projectfolder)
		
		entry={'ide':'SW4STM32', 'project': name, 'folder': projectfolder, 'board':board, 'target':target, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex, 'lib':lib, 'a':a}
		ret.append(entry)
			
		return ret
		
	def binGeneration(self, path, e):
		"""
			copy binaries .bin .hex in appropriate folder
			
			binGeneration() function copy the bin file to the appropriate Binary/
			folder and generates the corresponding .hex file through the 
			objcopy file
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				e:          the list of items that were returned from the compile phase
			Returns:
				a list of binaries generated in the compile phase
		"""
		projectfolder = e['folder']
		multi = path + '/Multi'
		if os.path.isdir(multi):
			binfolder     = projectfolder + "Binary/" + e['board'] + "/"
		else:
			binfolder     = projectfolder + "Binary/"
		
		if not os.path.isdir(binfolder):
			os.makedirs(binfolder)

		target = e['target']
		
		if len(e['bin']) > 0:
			if target == '-ALL':
				targetlist = e['bin']
			else:
				targetlist = [ target ]
			for bin in targetlist:
				target=os.path.split(os.path.dirname(bin))[1]
				filename_bin = binfolder + e['project'] + "_" +  target + ".bin"
				shutil.copy(bin, filename_bin)
				
				# generate the hex counterpart
				filename_hex = binfolder + e['project'] + "_" +  target + ".hex"
				#implement tool for bin -> hex conversion
				# $objcopy -I binary $binary_file -O ihex $hex_file --change-addresses 0x08000000
				cmdstring = self._compdir + "/arm-none-eabi-objcopy -I binary " + filename_bin + " -O ihex " + filename_hex + " --change-addresses 0x08000000"
				try:
					retval = check_output( cmdstring, shell=True )
				except subprocess.CalledProcessError:
					print(" ERROR executing the command ")
					print("       " + cmdstring )
		
		return [ filename_bin, filename_hex ]


	def clean(self, path, type, board, name, target):
		"""
			clean the given project 
			
			compile function calls the IDE to clean the project, 
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
		"""
		return 0

class SW4STM32_M(Ide):
	"""
		The SW4STM32 class is derived from the Ide abstract class and 
		provides support for the System Workbench IDE.
	"""
	_executable=[]
	_Folder='SW4STM32'
	_Extension='.cproject'
	_SW4_workspace='.__workspace'
	_environ=""
	
	def __init__(self):
		"""
		Initializes the environment
		
		__init__ setup the environment and raises an exception if it does
		not find what it is searching: the SystemWorkbench eclipsec executable,
		a make and arm-none-eabi-gcc binaries
		
		Args:
				self:  		self of the given object
		"""
		sw=self.findPattern('eclipsec.exe','c:/Ac6/SystemWorkbench/')
		if len(sw) != 1:
			raise
		
		self._executable = sw[len(sw)-1]
		
		sw4dir='c:/Ac6/SystemWorkbench/plugins'
		if os.path.isdir(sw4dir):
			make=self.findList('make.exe', sw4dir)
			if len(make) < 1:
				print('Error in finding make.exe command')
				exit(1)
			compiler=self.findList('arm-none-eabi-gcc.exe', sw4dir)
			if len(compiler) < 1:
				print('Error in finding make.exe command')
				exit(1)
			makedir=os.path.dirname(make[len(make)-1])
			makedir=makedir.replace('/', '/')
			makedir=makedir.replace('c:', '/c')
			compdir=os.path.dirname(compiler[len(compiler)-1])
			compdir=compdir.replace('/', '/')
			compdir=compdir.replace('c:', '/c')
			self._environ= makedir + ':' + compdir
		else:
			print('Something wrong with Ac6 installation')
			raise TestError()

				
	def compile(self, path, type, board, name, target, output):
		"""
			compile the given projct and returns the generated binary
			
			compile function calls the IDE to compile the project, raising an
			error if the project fails (printing only number of found warnings)
			and returns a list of filenames of the created binaries
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be compiled
				output:		a filename where to store the output
			Returns:
				a list of binaries generated in the compile phase
		"""
		ret = []
		project=self.findProject(path, type, board, name)
		# project not found or not existing
		if len(project) == 0:
			return ret
		binstore=[]
		projectfolder=os.path.dirname(project)
		projectfolder=os.path.realpath(projectfolder)
		
		if os.path.isdir(self._SW4_workspace):
			shutil.rmtree(self._SW4_workspace)
			
		# this is for some problems of Eclipse when dealing with msysgit bash
		if os.environ.get('MAKE_MODE') == None:
			epath=''
		else:
			print('SORRY, won\'t work with msysgit shell')
			
		
		if target == "-ALL":
			cmdstring = "\"" + self._executable + "\"  --launcher.suppressErrors -nosplash -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + self._SW4_workspace + epath + " -import " + projectfolder + " -cleanBuild all"
		else:
			cmdstring = "\"" + self._executable + "\"  --launcher.suppressErrors -nosplash -consolelog -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data " + self._SW4_workspace + epath + " -import " + projectfolder + " -cleanBuild " + name + "/" + target
			
		num_error = 0
		num_warn  = 0
		try: 
			print("--SW4  [ " + board + " ]: compiling " + name + ' for configuration ' + target )
			retval=check_output( cmdstring, shell=True )
		except subprocess.CalledProcessError as e:
			print(" ERROR executing the command ")
			print("       " + cmdstring )
			with open(output, 'w') as f:
				f.write(str(e.output))
			num_error = -1

		if num_error == 0:
			retval=str(retval)
			num_warn=retval.count('arning')
		
		bin=self.findPattern('*.bin', projectfolder)
		hex=self.findPattern('*.hex', projectfolder)

		entry={'ide':'SW4STM32', 'project': name, 'folder': projectfolder, 'board':board, 'target':target, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex': hex}

		ret.append(entry)
		return ret
		
	def clean(self, path, type, board, name, target):
		"""
			clean the given project 
			
			compile function calls the IDE to clean the project, 
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
		"""
		return 0

class SW4STM32(SW4STM32_W if platform.system() == "Windows" else SW4STM32_L if platform.system() == "Linux" else SW4STM32_M):
	"""
		The SW4STM32 class is derived from the Ide abstract class and 
		provides support for the System Workbench IDE.
	"""
	
	def __str__(self):
		"""
		returns the class name
		
		Args:
				self:  		self of the given object
		Returns:
				a string containing the class name
		"""
		return "SW4STM32"
	
	
	def configurations(self):
		pass
		
	def findProject(self, path, type, board, name):
		"""
			Returns a single project name
			
			findProject is a function that is returns the filename for the current System Workbench project
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
			Returns:
				a string containing path to current project filename
		"""
		return super(self.__class__, self).findProject( path, type, board, name, self._Folder, self._Extension )
	
	def findTargets(self, projname):
		"""
			returns the found targets in the XML file
			
			findProject is a function that is specialized in the IDEs and searches 
			into the project file the targets that are present and could be compiled
			
			Args:
				self:  		self of the given object
				projname:   the project name where to search
			Returns:
				a list of targets for the current project
		"""
		targetlist=[]
		with open(projname) as f:
			et = ElementTree.parse(f)
			for element in et.findall('storageModule/configuration'):
				targetlist.append(element.attrib['configurationName'])
		return targetlist
	
	def findSupportedBoards(self, path, type, name):
		"""
			returns a list of supported boards
			
			findSupportedBoards is a function that searches all the boards that
			are present in the specific subdirectory and list them
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				name:	 	project filename
			Returns:
				a list of boards that are supported
		"""
		return super(self.__class__, self).findSupportedBoards(path, type, name, self._Folder)
	
	def flash(self):
		pass
	
