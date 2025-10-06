import streamlit as st
import re

st.set_page_config(page_title="Đăng ký tài khoản", page_icon="📧", layout="centered")

st.title("📧 Đăng ký Tài Khoản")

# --- Nhập Email ---
email = st.text_input("Địa chỉ Email", placeholder="Nhập email theo mẫu hợp lệ...")

# --- Nhập Mật khẩu ---
password = st.text_input(
    "Mật khẩu",
    placeholder="Nhập mật khẩu theo quy tắc trên...",
    type="password"
)

# --- Kiểm tra định dạng Gmail ---
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@gmail\.com$"
    return re.match(pattern, email)

# --- Kiểm tra độ mạnh mật khẩu ---
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # Ít nhất 1 chữ hoa
        return False
    if not re.search(r"[a-z]", password):  # Ít nhất 1 chữ thường
        return False
    if not re.search(r"[0-9]", password):  # Ít nhất 1 số
        return False
    if not re.search(r"[@$!%*?&]", password):  # Ít nhất 1 ký tự đặc biệt
        return False
    return True

# --- Khi bấm nút ---
if st.button("Tạo Tài Khoản"):
    if not is_valid_email(email):
        st.error("❌ Email của bạn không hợp lệ. Vui lòng kiểm tra định dạng (ví dụ: ten.ban@gmail.com).")
    elif not is_valid_password(password):
        st.warning("⚠️ Mật khẩu không đáp ứng các yêu cầu về độ mạnh (8 ký tự, hoa, thường, số, đặc biệt).")
    else:
        st.success("🎉 Tạo tài khoản thành công!")
        st.balloons()
