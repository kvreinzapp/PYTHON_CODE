text = "X-DSPAM-Confidence:    0.8475"
position = text.find(':')
print(position)
end = text.find('5', position)
print(end)
target = text[position + 1:end]
target_no_space = target.strip()
print(float(target_no_space))
