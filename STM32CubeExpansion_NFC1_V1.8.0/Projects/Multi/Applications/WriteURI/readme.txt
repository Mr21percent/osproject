/**
  @page WriteURI Readme file
 
  @verbatim
  ******************** (C) COPYRIGHT 2016 STMicroelectronics *******************
  * @file    WriteURI/readme.txt 
  * @author  MMY Application Team
 * @version	1.8.0
 * @date	10-October-2018
  * @brief   This application write a simple URI containing "http://st.com" 
  *          to the M24SR expansion board.
  ******************************************************************************
  *
  * Redistribution and use in source and binary forms, with or without modification,
  * are permitted provided that the following conditions are met:
  *   1. Redistributions of source code must retain the above copyright notice,
  *      this list of conditions and the following disclaimer.
  *   2. Redistributions in binary form must reproduce the above copyright notice,
  *      this list of conditions and the following disclaimer in the documentation
  *      and/or other materials provided with the distribution.
  *   3. Neither the name of STMicroelectronics nor the names of its contributors
  *      may be used to endorse or promote products derived from this software
  *      without specific prior written permission.
  *
  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
  * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
  * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
  * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
  * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
   @endverbatim

@par Description

This directory contains a set of source files that implement a simple 
"www.st.com" example based on M24SR URI NDEF message exchange with
smartphone devices.

@note Care must be taken when using HAL_Delay(), this function provides accurate delay (in milliseconds)
      based on variable incremented in SysTick ISR. This implies that if HAL_Delay() is called from
      a peripheral ISR process, then the SysTick interrupt must have higher priority (numerically lower)
      than the peripheral interrupt. Otherwise the caller ISR process will be blocked.
      To change the SysTick interrupt priority you have to use HAL_NVIC_SetPriority() function.
      
@note The application need to ensure that the SysTick time base is always set to 1 millisecond
      to have correct HAL operation.

@par Directory contents 

  - WriteURI/Inc/main.h                   Main config file
  - WriteURI/Inc/cube_hal.h               file to manage Cube SW family used
  - WriteURI/Inc/stm32fXxx_hal_conf.h     Library Configuration file
  - WriteURI/Inc/stm32fXxx_it.h           Header for stm32fXxx_it.c
  
  - WriteURI/Src/main.c                   Main program file
  - WriteURI/Src/stm32fXxx_it.c           STM32FXxx Interrupt handlers
  - WriteURI/Src/system_stm32fXxx.c       STM32FXxx system file
 
@par Hardware and Software environment 


  - This example runs on STM32L053R8, STM32L152RE, STM32L476RG, STM32F030R8, STM32F072RB, STM32F103RB, STM32F302R8 and STM32F401RE devices.
    
  - This application has been tested with STMicroelectronics:
    STM32L0xx-Nucleo RevC
    STM32L1xx-Nucleo RevC
    STM32L4xx-Nucleo RevC	
    STM32F0xx-Nucleo RevC
    STM32F1xx-Nucleo RevC
    STM32F3xx-Nucleo RevC
    STM32F4xx-Nucleo RevC
    boards and can be easily tailored to any other supported device 
    and development board.

  - STM32LXxx-Nucleo and STM32FXxx-Nucleo RevC Set-up    
    - Connect the Nucleo board to your PC with a USB cable type A to mini-B 
      to ST-LINK connector (CN1).
    - Please ensure that the ST-LINK connector CN2 jumpers are fitted.

@par How to use it ? 

In order to make the program work, you must do the following :
  - Open your preferred toolchain 
  - Rebuild all files and load your image into target memory
  - Run the example
 
 * <h3><center>&copy; COPYRIGHT STMicroelectronics</center></h3>
 */
