my_text = "Reviver"

print(my_text.lower() == my_text.lower()[::-1])

def is_palindrome(text):
	start = 0
	end = len(text) - 1
	while start < end:
		if text[start] != text [end]:
			return False 
		start += 1
		end -= 1
	return True
	
print (is_palindrome(my_text.lower()))
