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
