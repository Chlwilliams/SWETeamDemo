import streamlit as st
from code_analyze import CodeAnalyze

import radon.raw as rr
import radon.metrics as rm
import radon.complexity as rc



def main():
    st.title("Static Code Analysis App")

    with st.form(key="myform"):
        raw_code = st.text_area("Enter Code Here")
        submit_button = st.form_submit_button(label="Analyze")


    tab1, tab2, tab3, tab4 = st.tabs(["Code Analysis", "test", "test", "test"])

    if submit_button: 

        try:
            compile(raw_code,"<string>","exec")
        except Exception as e:
            st.error(f"There was a error on" )
            return

        analyzer = CodeAnalyze(raw_code)

        with tab1:
            st.subheader("Code Analysis")
            with st.expander("Orginal Code"):
                st.code(raw_code)
        
        analyzer.analyze_code()
        analyzer.metrics_calc()
        analyzer.hals_metrics()
        


        




                

    


if __name__ == "__main__":
    main()