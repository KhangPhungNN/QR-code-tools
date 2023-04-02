# QR code tools

<summary><strong>Cách tải và mở File</strong></summary>
  
Chương trình được viết bằng ngôn ngữ lập trình python và chưa được build thành file có đuôi “.exe” để chạy trên windows. Vì thế cần tải python về để chạy file, cụ thể các bước tải như sau:

<details>
<summary>Dùng File Check_and_install_python.cmd trong chương trình để tự động cài Python</summary>

- Chạy file dưới quyền Admin
- Đợi khoảng 4-5 phút để File chạy
- Sau khi hiện dòng chữ "Press any key to continue . . .", nhấn bất kì phím để thoát chương trình.

</details>

<details>
<summary>Tải Python theo cách thủ công</summary>

- Lên trang chủ: python.org để tải
- Chọn phần Downloads
- Chọn Downloads for (windows hoặc macOS) [Bản mới nhất khi file này được viết đang là 3.10.4]
- Bật file setup, nhấn add python 3.x.x to PATH (ở dòng dưới) <ảnh: osstuff.com>

  ![image](https://user-images.githubusercontent.com/97179275/168414883-69a2063a-5a1a-4e8a-9fe5-36a9f01706a0.png)

- Nhấp đúp vào file có tên AIO.py
  
</details>

Video demo QR-code-tools -> [Demo QR-code-tools](https://www.youtube.com/watch?v=NV8Up8Iwtsw)

>***Nếu làm theo những cách trên không được, liên hệ tôi bằng tài khoản facebook này: [MyFacebook](https://www.facebook.com/KhangPhungNN).***
  

# QR code (Quick response code) là gì ?

<summary><strong>Định nghĩa và ví dụ của QR code (Quick response code)</strong></summary>
  
- QR Code (mã QR) là viết tắt của Quick response code (Tạm dịch: Mã phản hồi nhanh), hoặc có thể gọi là Mã vạch ma trận (Matrix-barcode) hay Mã vạch 2 chiều (2D). Đây là một dạng thông tin được mã hóa để hiển thị sao cho máy có thể đọc được. QR Code xuất hiện lần đầu tiên vào năm 1994, được tạo ra bởi Denso Wave (công ty con của Toyota). QR Code bao gồm những chấm đen và ô vuông mẫu trên nền trắng, có thể chứa những thông tin như URL, thời gian, địa điểm của sự kiện, mô tả, giới thiệu một sản phẩm nào đó,... QR Code cho phép quét và đọc mã nhanh hơn bằng các thiết bị như máy đọc mã vạch hoặc điện thoại có camera với ứng dụng cho phép quét mã, vô cùng tiện lợi cho người dùng.
- Lấy ví dụ về một mã QR code:

  ![th](https://user-images.githubusercontent.com/97179275/148724072-e3a12b41-2e9b-480b-b4a9-151f5b90e20f.jpg)

- Hoặc là file có tên TEST.jpg cũng là một mã QR code.
- Bạn có thể dịch được mã QR code này thông qua phần Convert QR code to text có trong chương trình của tôi.
  

# Cách dùng QR code tools của mình

<summary><strong>Các phần chính và ví dụ trong chương trình</strong></summary>
  
- Mở File bằng cách như bước ở phần trên. Nếu bạn không mở được File, vui lòng liên hệ tôi bằng tài khoản facebook này: [MyFacebook](https://www.facebook.com/KhangPhungNN).
- Khi mở lên, bạn cứ để nó chạy, đến khi hiện tới phần: "Checking module finish !, Welcome to my programme !"
- Sau đó, bạn sẽ thấy màn hình chính: 

  ![image](https://user-images.githubusercontent.com/97179275/148739593-e5761e9a-d8f5-4a36-9c25-e7450b18e0c5.png)

- Chương trình gồm 4 phần:
    - 2 phần chính: Convert QR code to text (Chuyển đổi mã QR thành văn bản) và Convert text to QR code (Chuyển đổi văn bản thành mã QR).
    - 2 phần phụ: Exit (Thoát) và View error code (Xem mã lỗi).
> Để thực thi những phần trên, bạn nhập số tương ứng với nó vào rồi nhấn Enter.


### Phần 1 Convert QR code to text (Chuyển đổi mã QR thành văn bản):

<details>
<summary><strong>Phần 1 & ví dụ</strong></summary>
  
- Khi enter sẽ xuất hiện dòng chữ: "Enter file name:", bạn nhập tên file vào đó (Lưu ý: tên file không được viết có các kí tự đặc biệt, viết không dấu và không khoảng trắng, có thể dùng dấu ghạch dưới " _ " thay cho khoảng trắng; File có định dạng hình ảnh và được đặt cùng địa chỉ với file AIO.py; Không được đổi tên thư mục Data)
- Sau đó trên màn hình sẽ hiện nội dung của mã, cấu trúc như sau: "Output: [Nội dung của mã QR]".
- Nhấn Enter để thoát.

  ![Screen Shot 2022-01-18 at 16 58 10](https://user-images.githubusercontent.com/97179275/149915629-163854b5-a98b-409f-b708-0efed0461f4a.png)

</details>
  
### Phần 2 Convert text to QR code (Chuyển đổi văn bản thành mã QR):

<details>
<summary><strong>Phần 2 & ví dụ</strong></summary>
  
- Khi enter sẽ xuất hiện dòng chữ: "Enter the data will be converted: ", bạn nhập dữ liệu cần chuyển đổi qua QR code [được viết tự do, không yêu cầu hình thức, chỉ hỗ trợ định dạng UTF-8 (8-bit Unicode Transformation Format - Định dạng chuyển đổi Unicode 8-bit)].
- Bước tiếp theo, bạn nhập tên của file (tên file đặt là gì cũng được, lưu ý: tên không được có kí tự đặc biệt, ví dụ “:”,… và không được có dấu khoảng trắng, có thể thay khoảng trắng bằng dấu ghạch dưới " _ "), xong enter để thực thi. (Lấy ví dụ tên file: File_name)
- Sau đó sẽ hiện ra mã QR của bạn với nội dung mà bạn mới nhập ở bước trên.

  ![Screen Shot 2022-01-18 at 17 23 58](https://user-images.githubusercontent.com/97179275/149921422-f66e386a-c47c-4bc7-8651-f1ca971b2056.png)

</details>

### Phần 3 Exit (Thoát):

<details>
<summary><strong>Phần 3</strong></summary>
  
- Nhấn phím số 3 sau đó nhấn phím enter trên bàn phím để thực thi (công dụng của nó dùng để thoát chương trình).

</details>

### Phần 4 View error code (Xem mã lỗi):

<details>
<summary><strong>Phần 4</strong></summary>
  
- Nhấn phím số 4 sau đó nhấn phím enter trên bàn phím để thực thi (công dụng của nó dùng để xem mã lỗi để biết mình đang gặp lỗi nào, thường thì nó sẽ báo trên của sổ chương trình luôn, hoặc có thể liên hệ trực tiếp với mình bằng tài khoản facebook này: [MyFacebook](https://www.facebook.com/KhangPhungNN).)

</details>
  
