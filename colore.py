import streamlit as st

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_binary(rgb):
    return tuple(format(i, '08b') for i in rgb)

def app():
    st.title("16進数カラーコード変換アプリ")

    color_hex = st.text_input("16進数のカラーコードを入力してください", "#ffffff")

    if len(color_hex) == 7 and color_hex[0] == "#":
        rgb = hex_to_rgb(color_hex)
        binary = rgb_to_binary(rgb)

        st.write(f"""
            <style>
                body {{
                    background-color: {color_hex};
                }}
            </style>
        """, unsafe_allow_html=True)

        st.write(f"RGB: {rgb}")
        st.write(f"Binary: {binary}")
    else:
        st.write("正しい形式で入力してください（例：#ffffff）")

if __name__ == '__main__':
    app()
import streamlit as st

def decimal_to_hex(decimal_value):
    return hex(decimal_value)[2:].zfill(2)

def main():
    st.title('RGB to Hexadecimal Converter')

    r = st.number_input('Enter the decimal value for R (0-255)', 0, 255)
    g = st.number_input('Enter the decimal value for G (0-255)', 0, 255)
    b = st.number_input('Enter the decimal value for B (0-255)', 0, 255)

    hex_r = decimal_to_hex(r)
    hex_g = decimal_to_hex(g)
    hex_b = decimal_to_hex(b)

    st.write(f'Hexadecimal conversion: #{hex_r}{hex_g}{hex_b}')

if __name__ == '__main__':
    main()
