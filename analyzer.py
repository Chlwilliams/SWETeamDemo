import streamlit as st
from code_analyze import CodeAnalyze
from code_quality import CodeQuality


def main():
    st.title("Static Code Analysis App")

    with st.form(key="myform"):
        raw_code = st.text_area("Enter Code Here")
        submit_button = st.form_submit_button(label="Analyze")


    tab1, tab2, tab3, tab4 = st.tabs(["Code Analysis", "Code Quality", "test", "test"])

    if submit_button:
        errors = []

        qualityCheck = CodeQuality(raw_code)
        analyzer = CodeAnalyze(raw_code)

        errors = qualityCheck.qualitycheck()

        try:
            compile(raw_code,'<string>','exec')
        except:
            st.error("Try again!")
            return
        
        with tab1:
            st.subheader("Code Analysis")
            with st.expander("Orginal Code"):
                st.code(raw_code)
            analyzer.analyze_code()
            analyzer.metrics_calc()
            analyzer.hals_metrics()

        with tab2:
            with st.expander("Orginal Code"):
                st.code(raw_code)
            if errors:
                with st.expander("Quality Issues"):
                    for error in errors:
                        st.error(error)
            else:
                st.write("No Suggestions.")

if __name__ == "__main__":
    main()
