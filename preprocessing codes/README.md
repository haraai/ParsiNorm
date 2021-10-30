<div dir='ltr' align='left'>

# pre-processing

according to chapter 26, Automatic Speech Recognition and Text-to-Speech these normalizations must be done:
TTS systems require text normalization preprocessing for handling non-standard words: numbers, monetary amounts, dates, and other concepts that are verbalized differently than they are spelled

Here are all Functions that are implemented:

General Normalization:

•	Converting HTML tags to text

•	Converting All Persian Characters to a particular format 

•	Converting All English Characters to a particular format 

•	Converting All Numbers to a particular format of Persian Numbers then we convert it to text

•	 Converting Some Arabic Words that are common in Persian to Persian Particular format

•	Converting All punctuations have the same meaning but different shapes to a particular format

•	Converting Math character to Persian numbers and style

•	Converting Some Special English Characters to a particular format

•	Removing Emojis

•	Separate sentences 

Text-To-Speech Normalization

•	Replace all symbols with text

	Such as star(*) square(#) Degree(°) Percent(%) 


•	Replace common currency with their readable text format

•	Replace Math symbols with Persian readable text

•	Replace Abrravations with how it is pronounced

	English Abrrevation to Persian readable format

	Abbreviation of different topics such as time, date, law, books, etc 


•	Converting Date to text

•	Converting Time to text

•	Converting all numbers to text

•	Converting URLs to a readable format. for example, “dot” instead of  “.” ,  “do noghte slash slash” instead of “://” (actually it is the way we pronounce these punctuations in Persian when we want to read an Email Address) and removing unnecessary parts of URLs it is the part which comes after the second / which is after domain part of URL

•	Converting Emails to a readable format.  For example, “dot” Instead of “.” ,  “at” instead of “@” , “dash” instead of “-” and “underline” instead of “_”

•	Converting Currency signs to the Persian text

•	Detect telephone Numbers and convert to different reading format

•	Detect Persian National Code and Convert to Text

•	Detect card number and convert to text

•	Detect Sheba and convert to text




