import setuptools
with open ("README.MD","r") as f:
    long_des=f.read()

setuptools.setup(name="ten",version="0.0.1",author="Bavishyaa",author_email="bavishyaa1994@gmail.com",
                 description="Armstrong No. Find",long_description=long_des,long_description_content_type="text/markdown",
                 url="https://github.com/Bavishyaa/Python-Capsule",packages=setuptools.find_packages(),classifiers=["programming language :: python :: 3","operationg system :: os independent"]
                 ,python_requires=">=3.6")
