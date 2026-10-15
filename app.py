import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

# Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")


# 1. TẠO DỮ LIỆU 10 SINH VIÊN


data = {
    "Họ tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Văn Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Em",
        "Vũ Thị Hà",
        "Đặng Văn Hùng",
        "Bùi Thị Lan",
        "Đỗ Văn Minh",
        "Ngô Thị Ngọc"
    ],
    "Chuyên cần": [9, 8, 10, 7, 8, 9, 6, 10, 8, 9],
    "Giữa kỳ": [8, 7, 9, 6, 8, 9, 5, 8, 7, 10],
    "Cuối kỳ": [9, 8, 9, 7, 8, 10, 6, 9, 8, 9]
}

df = pd.DataFrame(data)


# 2. TÍNH ĐIỂM TỔNG KẾT


df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
)


# 3. XẾP LOẠI SINH VIÊN


def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)


# 4. HIỂN THỊ BẢNG ĐIỂM


st.header("1. Bảng điểm sinh viên")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)


# 5. THỐNG KÊ KẾT QUẢ


st.header("2. Thống kê kết quả học tập")

diem_trung_binh = df["Tổng kết"].mean()

sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]

so_sv_dat = (df["Tổng kết"] >= 5).sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Điểm trung bình lớp",
    f"{diem_trung_binh:.2f}"
)

col2.metric(
    "Điểm cao nhất",
    f"{sv_cao_nhat['Tổng kết']:.1f}"
)

col3.metric(
    "Điểm thấp nhất",
    f"{sv_thap_nhat['Tổng kết']:.1f}"
)

col4.metric(
    "Số sinh viên đạt",
    f"{so_sv_dat}/10"
)

st.write(
    f"**Sinh viên điểm cao nhất:** "
    f"{sv_cao_nhat['Họ tên']}"
)

st.write(
    f"**Sinh viên điểm thấp nhất:** "
    f"{sv_thap_nhat['Họ tên']}"
)


# 6. CHỌN SINH VIÊN BẰNG SELECTBOX


st.header("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn họ tên sinh viên:",
    df["Họ tên"]
)

# Lấy thông tin sinh viên được chọn
sv = df[df["Họ tên"] == ten_sv].iloc[0]

st.subheader(f"Thông tin sinh viên: {ten_sv}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Điểm chuyên cần",
    f"{sv['Chuyên cần']:.1f}"
)

col2.metric(
    "Điểm giữa kỳ",
    f"{sv['Giữa kỳ']:.1f}"
)

col3.metric(
    "Điểm cuối kỳ",
    f"{sv['Cuối kỳ']:.1f}"
)

col4, col5 = st.columns(2)

col4.metric(
    "Điểm tổng kết",
    f"{sv['Tổng kết']:.1f}"
)

col5.metric(
    "Xếp loại",
    sv["Xếp loại"]
)


# 7. VẼ BIỂU ĐỒ CỘT


st.header("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    df["Họ tên"],
    df["Tổng kết"]
)

ax.set_title("BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")

ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


# 8. THÔNG TIN NGƯỜI TẠO ỨNG DỤNG


st.divider()

st.markdown(
    """
    <div style="text-align: center; font-size: 12px; color: gray;">
        Người tạo: Phùng Thái Đông Đông<br>
        MSSV: 064208005954
    </div>
    """,
    unsafe_allow_html=True
)       
