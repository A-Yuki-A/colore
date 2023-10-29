import streamlit as st

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))

def rgb_to_binary(rgb):
    return [format(i, '08b') for i in rgb]

def main():
    st.title('Color Converter')

    hex_color = st.text_input('Enter a Hex color code (with #):', '#ffffff')
    hex_color = hex_color.strip()

    if hex_color:
        try:
            rgb = hex_to_rgb(hex_color)
            binary = rgb_to_binary(rgb)

            st.write(f"RGB: {rgb}")
            st.write("RGB to Binary:")
            for i, color in enumerate(['Red', 'Green', 'Blue']):
                st.write(f"{color}: {binary[i]}")
            
            st.write('Displaying the color:')
            st.write('This is the color you chose:', hex_color)
            st.markdown(
                f'''
                <style>
                .color-box {{
                    height: 100px;
                    width: 100px;
                    background-color: {hex_color};
                }}
                </style>
                '''
            )
            st.markdown(f'<div class="color-box"></div>', unsafe_allow_html=True)

        except ValueError:
            st.error('Invalid Hex code. Please enter a valid Hex color code.')

if __name__ == '__main__':
    main()
