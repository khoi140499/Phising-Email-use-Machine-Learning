URLREGEX = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
URLREGEX_NOT_ALONE = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
FLASH_LINKED_CONTENT = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])+).*\.swf"
HREFREGEX = '<a\s*href=[\'|"](.*?)[\'"].*?\s*>'
IPREGEX =  r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b"
EMAILREGEX = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
HOTWORD = r"account|update|sercurity|click|dolar|apply|call|deal|get|offer|action|order|billion|cash|shop|money|buy|shopper|earn|$|best price|bank|free|%|important|resent|verify|please|credit|address|infomation|update|user|access"
LISTSUBJECT=r"account|update|security|important|resent|notice|verify|please|verification|credit|bank|online"
PATH=r".pdf|.zip|.exe|.rar|.rtf|.dat|.txt|.dll|.7z|.doc|.docx|.jpg|.gif|.xls"
