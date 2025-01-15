import streamlit as st
import pyshorteners
st.warning("dokdox 에서 만든 이 페이지는 개발중인 기능으로 아직 완성되지 않았습니다.오류가 발생할수도 있습니다.")
st.link_button("dokdox 날씨 보기","https://dokdox.com")
st.link_button("dokdox 무료 ai 사용하기","https://dokdox.streamlit.app")
st.title("Dokdox url shorteners")
st.write("welcom to dokdox url shortners service.")


url = st.text_input("단축할 URL을 입력하세요:")


if st.button("URL 단축시작하기(약 1초 미만 소요)"):
    if url:
        # pyshorteners 라이브러리 사용하여 URL 단축
        shortener = pyshorteners.Shortener()
        short_url = shortener.bitly.short(url)

        st.write(f"단축된 URL: {short_url}")
    else:
        st.warning("URL을 입력해주세요.")