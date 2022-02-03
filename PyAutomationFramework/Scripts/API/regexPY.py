
import re

text="Hi abc @ gmail.com, are you from India?"
print("Original text : %s"% text)
d=re.sub('[?@.,]'," ",text)
print("replaced text is : %s"% d)


text="Hi abc @!@#@$#%$&^*^&%^@ gmail.com, are you from India?"
print("Original text : %s"% text)
d=re.sub('[?@.,#$%^]',"",text)
print("replaced text is : %s"% d)