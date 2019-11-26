# -*- coding: utf-8 -*-


def readQR():

	from imutils.video import VideoStream
	from pyzbar import pyzbar
	import argparse
	import datetime
	import imutils
	import time
	import cv2

	ap = argparse.ArgumentParser()
	ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
		help="path to output CSV file containing barcodes")
	args = vars(ap.parse_args())

	print("[INFO] starting video stream...")
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)


	csv = open(args["output"], "w")
	found = set()

	barcodes=[]
	while True:

		frame = vs.read()
		frame = imutils.resize(frame, width=400)


		barcodes = pyzbar.decode(frame)
		for barcode in barcodes:

			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
			
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type

			text = "{} ({})".format(barcodeData, barcodeType)
			cv2.putText(frame, text, (x, y - 10),
                                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

			if barcodeData not in found:
				csv.write("{},{}\n".format(datetime.datetime.now(),
					barcodeData))
				csv.flush()
				found.add(barcodeData)

		cv2.imshow("Barcode Scanner", frame)
		key = cv2.waitKey(1) & 0xFF
		if barcodes != []:
			cv2.destroyWindow("Barcode Scanner")
			break


	price,store=barcodes[0][0].split('##')
	print(price, store)


'''
global i_have_card
i_have_card=[['이마트 KB카드', '<결제코드1>'],['삼성 S클래스 카드', '<켤제코드2>']]
def plus_card(name,signal):
    for i in range(len(i_have_card)):
        if name==i_have_card[i][0]:
            return 0
    list=[]
    list.append(name)
    list.append(signal)
    i_have_card.append(list)

def rm_card(name):
    i = 0
    while i < len(i_have_card) :
        if(i_have_card[i][0] == name) :
            i_have_card.pop(i)
            i -= 1
        i += 1
'''
