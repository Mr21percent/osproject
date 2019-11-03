import qrcode
img = qrcode.make('첫 큐알코드 하지만 아직 저장장소를 조정하는 방법을 모르겠..')
#img.save("파일명.파일확장자") 여기서 뭘 건드려야할거같긴함.
img.save("first.png")

#혹은 자세한 부분을 건드리기 위해
qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
#QRCode객체를 만들어 상세하게 제어가능.

qr.add_data("yeah it's add some more infromation 정보를 더하자!")
#데이터 추가

