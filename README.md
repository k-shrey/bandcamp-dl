## bandcamp-dl
Simple script to download music from bandcamp.com

## Installation
- Clone the repo or download the zip 
- Make sure you have pip installed 
- cd to the folder and run 
` pip install - r requirements.txt `

## Usage
#### Options:
> ` --url [URL]       Link to album/song page`       
> `--dir [DIRECTORY] Location to save tracks, current working directory is the default download location`       

#### Example: 
> `python3 bandcamp-dl.py --url URL --dir "D:/music"`        
> `python3 bandcamp-dl.py --url URL --dir "/home/<username>/Music"`       

## Dependencies
BeautifulSoup - HTML parsing    
Requests - for retrieving HTML

