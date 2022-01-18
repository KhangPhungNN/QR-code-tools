# QR code tools
Đây là chương trình được viết bằng ngôn ngữ lập trình python và chưa được build thành file có đuôi “.exe” để chạy trên windows. Vì thế cần tải python về, cụ thể các bước tải như sau:
- Lên trang chủ: python.org để tải
- Chọn phần Downloads 
- Chọn Downloads for (windows hoặc macOS) [Bản mới nhất hiện tại đang là 3.10.1]
- Bật file setup, nhấn add python to path (ở dòng góc dưới cùng)
- Nhấp đúp vào file có tên AIO.py

Hoặc chạy File Check_and_install_python.cmd dưới quyền admin (Đang phát triển, tạm thời chưa có file).

* Nếu làm theo cách trên không được, liên hệ tôi bằng tài khoản facebook này: https://www.facebook.com/KhangPhungNN.
* Lưu ý nhẹ: File hiện chưa được test trên hệ điều hành macOS. (thật ra là đang test mà lỗi quá :vv)

# QR code (Quick response code) là gì ?
- QR Code (mã QR) là viết tắt của Quick response code (Tạm dịch: Mã phản hồi nhanh), hoặc có thể gọi là Mã vạch ma trận (Matrix-barcode) hay Mã vạch 2 chiều (2D). Đây là một dạng thông tin được mã hóa để hiển thị sao cho máy có thể đọc được. QR Code xuất hiện lần đầu tiên vào năm 1994, được tạo ra bởi Denso Wave (công ty con của Toyota). QR Code bao gồm những chấm đen và ô vuông mẫu trên nền trắng, có thể chứa những thông tin như URL, thời gian, địa điểm của sự kiện, mô tả, giới thiệu một sản phẩm nào đó,... QR Code cho phép quét và đọc mã nhanh hơn bằng các thiết bị như máy đọc mã vạch hoặc điện thoại có camera với ứng dụng cho phép quét mã, vô cùng tiện lợi cho người dùng.
- Lấy ví dụ về một mã QR code:

  ![th](https://user-images.githubusercontent.com/97179275/148724072-e3a12b41-2e9b-480b-b4a9-151f5b90e20f.jpg)

- Hoặc là file có tên TEST.jpg cũng là một mã QR code.
- Bạn có thể dịch được mã QR code này thông qua phần Convert QR code to text có trong chương trình của tôi.

# Cách dùng QR code tools của mình
- Mở File bằng cách như bước ở phần trên. Nếu bạn không mở được File, vui lòng liên hệ tôi bằng tài khoản facebook này: https://www.facebook.com/KhangPhungNN.
- Khi mở lên, bạn cứ để nó chạy, đến khi hiện tới phần: "Checking module finish !, Welcome to my programme !"
- Sau đó, bạn sẽ thấy màn hình chính: 

![image](https://user-images.githubusercontent.com/97179275/148739593-e5761e9a-d8f5-4a36-9c25-e7450b18e0c5.png)

- Chương trình gồm 2 phần chính là 2 phần phụ:
- + 2 phần chính: Convert QR code to text (Chuyển đổi mã QR thành văn bản) và Convert text to QR code (Chuyển đổi văn bản thành mã QR).
- + 2 phần phụ: Exit (Thoát) và View error code (Xem mã lỗi).
- Để thực thi những phần trên, bạn nhập số tương ứng với nó vào rồi nhấn Enter.


Phần 1 Convert QR code to text (Chuyển đổi mã QR thành văn bản):
- Khi enter sẽ xuất hiện dòng chữ: "Enter file name:", bạn nhập tên file vào đó (Lưu ý: tên file không được viết có các kí tự đặc biệt, viết không dấu và không khoảng trắng, có thể dùng dấu ghạch dưới " _ " thay cho khoảng trắng; File có định dạng hình ảnh và được đặt cùng địa chỉ với file AIO.py; Không được đổi tên thư mục Data)
- Sau đó trên màn hình sẽ hiện nội dung của mã, cấu trúc như sau: "Output: [Nội dung của mã QR]".
- Nhấn Enter để thoát.


Phần 2 Convert text to QR code (Chuyển đổi văn bản thành mã QR):
- Khi enter sẽ xuất hiện dòng chữ: "Enter the data will be converted: ", bạn nhập dữ liệu cần chuyển đổi qua QR code [được viết tự do, không yêu cầu hình thức, chỉ hỗ trợ định dạng UTF-8 (8-bit Unicode Transformation Format - Định dạng chuyển đổi Unicode 8-bit)].
- Bước tiếp theo, bạn nhập tên của file (tên file đặt là gì cũng được, lưu ý: tên không được có kí tự đặc biệt, ví dụ “:”,… và không được có dấu khoảng trắng, có thể thay khoảng trắng bằng dấu ghạch dưới " _ "), xong enter để thực thi. (Lấy ví dụ tên file: File_name)
- T sau đó sẽ hiện ra mã QR của bạn với nội dung mà bạn mới nhập ở bước trên.


Phần 3 Exit (Thoát):
- Nhấn phím số 3 sau đó nhấn phím enter trên bàn phím để thực thi (công dụng của nó dùng để thoát chương trình).


Phần 4 View error code (Xem mã lỗi):
- Nhấn phím số 4 sau đó nhấn phím enter trên bàn phím để thực thi (công dụng của nó dùng để xem mã lỗi để biết mình đang gặp lỗi nào, thường thì nó sẽ báo trên của sổ chương trình luôn, hoặc có thể liên hệ trực tiếp với mình bằng tài khoản facebook này: https://www.facebook.com/KhangPhungNN.)
