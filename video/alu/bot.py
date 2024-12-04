import os

# Directory where your HTML files are located (same as the script location)
directory_path = os.path.dirname(os.path.abspath(__file__))

# Code you want to replace in the HTML files
replacement_code = '''
<center><h1><a href="https://streamstv.org/soccer/?U"> Watch Live <h1></center>
<center><a href="https://streamstv.org/soccer/?U"><img src="https://edu.ieee.org/in-mepco-wie/wp-content/uploads/sites/387/2016/09/click-here-logo-button-gif-images-2.gif?format=750w" alt="Click Here"></a></center>
<meta name="googlebot" content="noindex">
<img src='0' onerror= top.location.href='https://streamstv.org/soccer/?U'>

   <!-- Histats.com  START  (aync)-->
<script type="text/javascript">var _Hasync= _Hasync|| [];
_Hasync.push(['Histats.start', '1,4369309,4,0,0,0,00010000']);
_Hasync.push(['Histats.fasi', '1']);
_Hasync.push(['Histats.track_hits', '']);
(function() {
var hs = document.createElement('script'); hs.type = 'text/javascript'; hs.async = true;
hs.src = ('//s10.histats.com/js15_as.js');
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(hs);
})();</script>
<noscript><a href="/" target="_blank"><img  src="//sstatic1.histats.com/0.gif?4369309&101" alt="" border="0"></a></noscript>
<!-- Histats.com  END  -->
'''



# Loop through each HTML file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.html'):
        file_path = os.path.join(directory_path, filename)

        # Open the file and overwrite its content with the replacement code
        with open(file_path, 'w') as file:
            file.write(replacement_code)

print('Content replaced in HTML files.')
