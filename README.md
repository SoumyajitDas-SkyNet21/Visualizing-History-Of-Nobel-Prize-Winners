# Visualizing the Nobel Prize Winners (1901-2024)
- This project analyzes and visualizes data on Nobel Prize winners from 1901 to 2024. The goal is to provide insights into historical trends, gender distribution, and other fascinating patterns within the Nobel Prize data through compelling visualizations.

# The Business Problem 

<b>The Challenge: </b> Despite the Nobel Prize being a globally recognized and prestigious award, a comprehensive, up-to-date, and interactive visualization of its historical data is not readily available. Many online resources offer fragmented views, static charts, or outdated information. This makes it difficult for researchers, journalists, and curious individuals to easily explore and find answers to questions like:
- What is the most commonly awarded gender and birth country?
- Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories ?
- Which decade and Nobel Prize category combination had the highest proportion of female laureates ?
- Who was the first woman to receive a Nobel Prize, and in what category?
- Which individuals or organizations have won more than one Nobel Prize throughout the years?
- In which year does the highest number of prizes were distributed ?
- Average Age of Laureates at the time of Award Ceremony
- Average Age of Laureates at the time of Award Ceremony by Category and Gender
- Which Organization was the most laureates associated with ?
- Nobel Prize Received by Individual Vs Organization ?
- How many Prizes were shared ?
- Contribution of Men and Women to Nobel Prize from 1901-2024
- Country of Origin of Laureates for each category 
- Youngest Winner of Nobel Prize
- Oldest Winner of Nobel Prize 
- Median Age of Nobel Laureates


<b>Our Solution</b>: This project addresses this gap by creating an automated pipeline that fetches the latest data and presents it through a series of clear, interactive, and insightful visualizations. This provides a single, reliable source for anyone interested in exploring the rich history of the Nobel Prize.

# Table of Contents
- Features

- Data Source and Methodology

- Libraries Used

- Results and Visualizations

- Contributing

- License


### Features
- <b>Real-time Data Collection:</b> A custom Python script fetches the latest Nobel Prize winner data directly from the official Nobel Prize API.

- <b>Data Preprocessing:</b> The script cleans, processes, and extracts key data points required for analysis.

- <b>Data Storage:</b> Stores the cleaned data in both JSON and CSV formats for easy use in various analytical workloads.

### Data Source and Methodology

- The core of this project is a custom Python script that fetches real-time data from the official Nobel Prize API- <b>https://api.nobelprize.org/2.1/nobelPrizes</b>

- The process is as follows:
    
    - The Python script connects to the API to collect raw data on all Nobel laureates.
    
    - The data is then pre-processed and cleaned to a suitable format for analysis.
    
    - These are the columns which were extracted -

        - laureate_id: A unique identification number assigned to each Nobel Prize winner.
        
        - awardYear: The year the Nobel Prize was officially awarded.
        
        - category: The specific field or discipline for which the prize was given (e.g., Physics, Literature, Peace).
        
        - prize: The name of the prize received.
        
        - motivation: The official reason or specific discovery/achievement for which the prize was awarded.
        
        - portion: Indicates the share of the prize received by the laureate, such as "1/2" or "1/3," when the award is shared among multiple winners.
        
        - laureate_type: Specifies whether the recipient is an "individual" or an "organization."
        
        - full_Name: The complete name of the laureate.
        
        - gender: The gender of the individual laureate.
        
        - birth_city: The city where the laureate was born.
        
        - birth_country: The country where the laureate was born.
        
        - birth_continent: The continent where the laureate was born.
        
        - organization_name: The name of the organization the laureate was affiliated with at the time of the award.
        
        - organization_city: The city of the organization the laureate was affiliated with.
        
        - organization_country: The country of the organization the laureate was affiliated with.
        
        - death_city: The city where the laureate passed away.
        
        - death_country: The country where the laureate passed away.
        
        - iso_alpha: The two-letter country code (ISO 3166-1 alpha-2) for the laureate's country of birth.
        
        - birth_date_datetime: The birth date of the laureate, in a machine-readable date-time format.
        
        - death_date_datetime: The death date of the laureate, in a machine-readable date-time format.
        
        - years_lived: The total number of years the laureate lived.
        
        - dateAwarded_datetime: The specific date on which the prize was awarded, in a machine-readable date-time format.
        
        - laureates_age_receiving_prize: The age of the laureate at the time they received the prize.

    - The final, cleaned dataset is stored in both JSON and CSV formats, making it ready for any analytical workload.
 
- ### Libraries Used -
    This project is built using Python and utilizes the following libraries:

    - pandas: Essential for data manipulation and analysis.
    
    - numpy: Used for numerical operations on the data.
    
    - matplotlib: A foundational library for creating static plots.
    
    - plotly: For creating interactive and dynamic visualizations.
    
    - datetime: To handle date and time-related data.
    
    - pycountry: To map and handle country information.
    
    - json: To parse and handle data from the API.
    
    - requests: To make HTTP requests to the Nobel Prize API.
 
- ### Results and Visualizations
- #### What is the most commonly awarded gender and birth country?
      - Gender Distribution: Our analysis shows an overwhelming majority of Nobel Prize winners are male, with 911 awarded to men, 65 to women, and 28 to organizations.
      - Birth Country: The USA, followed by the UK and Germany, has produced the most Nobel laureates, highlighting a concentration of awards in these nations.      
- <img src="Graphs/Gender Distribution of Laureates.png"/>
- <img src="Graphs/Most Common Birth Country of Laureates.png"/>

- #### Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories ?
      - Decade 2000 has the highest ratio of US-Born Winners to the total_winners
- #### Who was the first woman to receive a Nobel Prize, and in what category?
      - Marie Curie is the first women to receive a Nobel Prize in Physics
- #### In which year does the highest number of prizes were distributed ?
        - Year 2001 has the highest count of Nobel Prize Distribution
- <img src="Graphs/Years with Highest No. Of Prize Distributions.png"/>

- #### verage Age of Laureates at the time of Award Ceremony
     - The average age of male laureates at the time of the ceremony is 61, while for women it is slightly younger at 59.
- <img src="Graphs/Average Age Of Nobel Laureates - Male Vs Female.png"/>

- #### Average Age of Male Laureates at the time of Award Ceremony by Category 
      - Category-Specific Age Analysis: The data shows a significant spread in the average age of male laureates across different fields. The Economic Sciences laureates are the oldest on average at 66.62 years, while Physics laureates are the youngest at 57.87 years. The remaining categories fall between this range, with ages between 58 and 65.
- <img src="Graphs/Average Age Of Male Nobel Laureates across categories.png"/>
  
- #### Average Age of Female Laureates at the time of Award Ceremony by Category
      - The average age of female laureates also varies significantly by category. Women recognized in Economic Sciences are the oldest on average at 67.00 years, while those awarded the Nobel Peace Prize are the youngest at 51.47 years. This is notably younger than the average age for male peace laureates (63.32 years).
- <img src="Graphs/Average Age of Female Nobel Laureates.png"/>

- #### Which Organization was the most laureates associated with ?
        - The University of California leads the list of organizations associated with Nobel laureates, followed by Harvard University, MIT, Stanford University, and the University of Chicago.
- <img src="Graphs/Top-5 Organization with most Laureates.png"/>

- #### Nobel Prize Received by Individual Vs Organization
        - Our dataset shows that 976 prizes have been awarded to individuals, a stark contrast to the 28 awarded to organizations. This indicates that the Nobel Prize is overwhelmingly a recognition of personal achievement.
- <img src="Graphs/Distribution of Nobel Prize Received by Individual Vs Organization.png"/>

- #### How many Prizes were shared ?
      - A total of 356 prizes were awarded to a single individual. However, 335 prizes were split between two recipients (1/2), 238 were shared among three (1/3), and 75 were shared among four (1/4). This shows that collaboration is often at the heart of Nobel-winning achievements.
   
- <img src="Graphs/Prize Shared Distribution.png"/>

- #### Contribution of Men and Women to Nobel Prize from 1901-2024

- <img src="Graphs/Contribution of Men and Women towards Nobel Prize from 1901-2024.png">

- #### 



