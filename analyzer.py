import streamlit as st
from code_analyze import CodeAnalyze
from code_quality import CodeQuality
from security_analyze import SecurityCheck


def main():
    # title for streamlit
    st.title("Static Code Analysis App")

    with st.form(key="myform"):
        raw_code = st.text_area("Enter Code Here")
        submit_button = st.form_submit_button(label="Analyze")

    # analysis code sections: tab1 - code analysis, tab2 - codequality tab3 - vulnerabilities
    tab1, tab2, tab3 = st.tabs(["Code Analysis", "Code Quality", "Security Vulnerability"])

    if submit_button:
        errors = []
        testSecurity = []

        qualityCheck = CodeQuality(raw_code)
        analyzer = CodeAnalyze(raw_code)
        security = SecurityCheck(raw_code)

        errors = qualityCheck.qualitycheck()

        testSecurity = security.securityIssue()
    # test to see if code can be compliled
        try:
            compile(raw_code,'<string>','exec')
        except:
            st.error("Try again!")
            return
    # Tab1:  Code Analysis Section
        with tab1:
            st.subheader("Code Analysis")
            with st.expander("Orginal Code"):
                st.code(raw_code)
            analyzer.analyze_code()
            analyzer.metrics_calc()
            analyzer.hals_metrics()
    # Tab2 : Code Quality Section
        with tab2:
            st.subheader("Code Quality")
            with st.expander("Orginal Code"):
                st.code(raw_code)
            st.subheader("Issues")
            if errors:
                with st.expander("Quality Issues"):
                    for error in errors:
                        test = error.split(':')
                        st.error(f"Line: {test[2]}, Column: {test[3]}, Error: {test[4]}")
            else:
                st.write("No Suggestions.")
    # Tab3 : Security Vulnerability Detection
        with tab3:
            st.subheader("Security Vulnerability")
            with st.expander("Original Code"):
                st.code(raw_code)
            st.subheader("Security Risks")
            with st.expander("Issues"):
                for test in testSecurity:
                    st.write(test)


if __name__ == "__main__":
    main()
