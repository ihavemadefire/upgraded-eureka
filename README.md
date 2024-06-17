# Upgraded Eureka

Upgraded Eureka is a hacked together data pipline for ingesting data from PDFs that don't have text embedded in them. It is currently in developement and not suitable for public use.

## Steps
The steps in the pipeline are:
- Download the .pdf
- Change to .pdf to a .jpg
- Flatten the color values to make sure text isn't missed
- Use text recognition software to scrape text from the document.
- Store the text in a .txt file

## Future functionality
- Use Pandas to map to data frames
- Use Pandas to drop the information into a relational DB.