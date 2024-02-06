"""
If you run this app in conda environment follow this tutorial
Also, this application is run under Github spaces.
https://docs.streamlit.io/get-started/installation/community-cloud
"""

import pandas as pd
import streamlit as st 
# Library for graphs
import altair as alt
# To display the logo
from PIL import Image

# Logo image
image = Image.open("dna-logo.jpg")

# Display the image by allowing the image to expand the column width
st.image(image, use_column_width=True)

# Header of the application on the website
# the three *** display and hr
st.write("""
    # DNA Nucleotide Count Web App
    This app counts the nucleotide composition of query DNA!     
         
    ***
""")

################################
# Input Tex Box
################################

st.header("Enter DNA sequence")

# Sample DNA sequence
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# Content of the text area and height to display
sequence = st.text_area("Sequence Input", sequence_input, height=250)
# Split lines on each \n
sequence = sequence.splitlines()
# Read from line in the index 1 onwards. We don't use index 0
sequence = sequence[1: ] # Skips the sequence name (first line)
sequence = "".join(sequence) # Concatenates lists to string and removes spaces between each line

st.write("""
***
""")

# Prints the input DNA sequence 
st.header("INPUT (DNA query)")
sequence

# DNA nucleotide count
st.header("OUTPUT (DNA Nucleotide Count)")

### 1. Print Dictionary
st.subheader("1.Print dictionary")
def DNA_nucleotide_count(seq):
    d = dict([
        # Use the .count to count each occurrence
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C")),
    ])

    return d

X = DNA_nucleotide_count(sequence)

X

### 2. Print Text
st.subheader("2. Print text")
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display Data frame
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index")
df
# Rename the column 0 to count
df = df.rename({0: "count"}, axis="columns")
# Reset the index
df.reset_index(inplace=True)
df = df.rename(columns = {"index": "nucleotide"})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader("4. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x = "nucleotide",
    y = "count"
)

p = p.properties(
    width = alt.Step(80) # controls width of bar.
)

st.write(p)
