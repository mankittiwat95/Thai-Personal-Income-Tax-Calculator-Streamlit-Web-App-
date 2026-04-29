import streamlit as st

# ส่วนการสร้างหน้าจอ (Creativity)
st.title("💰 โปรแกรมจำลองภาษีคร่าวๆ")
st.subheader("จัดทำโดย: แมน (Kittiwat)")

col1, col2 = st.columns([1, 1])
with col1:
# ส่วนการรับข้อมูล (Input)
    container = st.container()
    container.write("### รายได้ของคุณรวมทั้งปี")
    salary = st.number_input("ใส่เงินเดือนของคุณ/เดือน (บาท)", value=15000, step=1000)
    bonus = st.number_input("โบนัสที่คาดว่าจะได้ (บาท)", value=0, step=1000)

# ส่วนการคำนวณ (Logic/Accounting)
total_income = (salary * 12) + bonus
expenses = 100000  # ค่าใช้จ่ายเหมา 50% แต่ไม่เกิน 1 แสน
deduction_me = 60000 # ค่าลดหย่อนส่วนตัว
net_income = total_income - expenses - deduction_me

# แสดงผลลัพธ์

# ส่วนการแสดงผล Output  ฝั่งขวา
with col2:
    container = st.container()
    container.write("### ผลการคำนวณ")
    st.write("")
    st.info(f" รายได้สุทธิ:{net_income:,.2f} บาท")
    tax = 0
    if net_income > 150000:
        taxable_5 = min(net_income - 150000, 150000)
        tax = tax + (taxable_5 * 0.05)
    if net_income > 300000:
        taxable_10  = min(net_income - 300000, 200000)
        tax = tax + (taxable_10 * 0.10)
    if net_income > 500000:
        taxable_15 = min(net_income - 500000, 250000)
        tax = tax + (taxable_15 * 0.15)
    if net_income > 750000:
        taxable_20 = min(net_income - 750000, 250000)
        tax = tax + (taxable_20 * 0.20)
    if tax == 0:
        st.success("🎉 คุณไม่ต้องเสียภาษี!")
    else:
        st.error(f"💸 ยอดที่ต้องจ่ายคือ: {tax:,.2f} บาท")

# สว่นอธิบายเพิ่มเติม (Expander) 
st.divider()
with st.expander("🔍 ดูวิธีคำนวณภาษีแบบขั้นบันได"):
    st.write("โปรแกรมนี้คำนวณตามอัตราภาษีเงินได้บุคคลธรรมดา:")
    st.write("- 0 - 150,000 บาทแรก: **ยกเว้นภาษี**")
    st.write("- 150,001 - 300,000 บาท: **ภาษี 5%**")
    st.write("- 300,001 - 500,000 บาท: **ภาษี 10%**")
    st.write("- 750,001 - 1,000,000 บาท: **ภาษี 20%**")
    

   




