#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
text = "X-DSPAM-Confidence:    0.8475"
space = text[text.find(':')+1:]
no_space = space.lstrip()
fnum=float(no_space)
print(fnum)
