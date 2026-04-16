import re
import os

files = ['design_system_definitivo.html', 'design_system.html']

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f'-- {f} --')
        # match href="...", src="...", url('...')
        # avoid http, https, #, mailto, tel, data:
        pattern = r'(href=[\'\"]|src=[\'\"]|url\([\'\"]?)(?!http|#|mailto|tel|data)(.*?)((?:[\'\"]\)?)?)'
        
        matches = re.findall(pattern, content)
        urls = set([m[1] for m in matches])
        for u in urls:
            # strip trailing quotes or parens if any got stuck
            clean_u = u.strip('\'")')
            print(clean_u)
            
    except Exception as e:
        print(f"Error reading {f}: {e}")
