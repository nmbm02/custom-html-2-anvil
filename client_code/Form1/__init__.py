from ._anvil_designer import Form1Template
from anvil import *

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
  # Hàm xử lý sự kiện khi nhấn btnInput

  def btnInput_click(self, **event_args):
    """This method is called when the button is clicked"""
    btnInput_clickk(self.txtInput, self.lblArray)
    pass

  def btnDelete_click(self, **event_args):
    """This method is called when the button is clicked"""
    btnDelete_clickk(self.lblArray)
    pass

  def btnSort_click(self, **event_args):
    """This method is called when the button is clicked"""
    btnSort_clickk(self.lblArray, self.lblSortArray)
    pass

  def txtInput_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
def btnInput_clickk(txtInput, lblArray):
    # Lấy dãy số từ textbox và kiểm tra tính hợp lệ
    input_numbers = txtInput.text.split()
    try:
        # Chuyển đổi các số thành số nguyên
        int_numbers = [int(x) for x in input_numbers]
        # Kiểm tra xem tất cả các số đều là số nguyên
        if all(isinstance(x, int) for x in int_numbers):
            # Thêm dãy số nguyên mới vào label lblArray
            lblArray.text += ' ' + ' '.join(map(str, int_numbers))
        else:
            alert("Vui lòng chỉ nhập số nguyên!", title="Lỗi")
    except ValueError:
        alert("Vui lòng chỉ nhập số nguyên!", title="Lỗi")

# Hàm xử lý sự kiện khi nhấn btnDelete
def btnDelete_clickk(lblArray):
    # Xóa tuần tự các số từ phải sang trái
    current_text = lblArray.text
    new_text = ' '.join(current_text.split()[:-1])
    lblArray.text = new_text

# Hàm xử lý sự kiện khi nhấn btnSort
def btnSort_clickk(lblArray, lblSortArray):
    # Lấy dãy số nguyên từ label lblArray và sắp xếp bằng insertion sort
    input_list = [int(x) for x in lblArray.text.split()]
    sorted_list = insertion_sort(input_list)
    # Hiển thị dãy số nguyên đã sắp xếp trên label lblSortArray
    lblSortArray.text = ' '.join(map(str, sorted_list))



    

    
