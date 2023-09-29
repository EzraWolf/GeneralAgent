# GeneralAgent

*README & Project In Progress*

General purpose LLM / GPT agent with low bloat, it simply does what it says.

Will clean up later
Define standard format for searching the web

Filter data for each dept. & role, using criteria, rules, and reason
This makes the *taxonomy* or context

Data stored in data warehouse / mart

Send to DSS (decision support system) agent to filter through *each depts* data in the data warehouse

Make note of what to look for later, so if you need to find data on task A, then you figure out what to look for (X, Y, Z) then you have a pointer for A for later

Taxonomy
- how do you give better context?
- text without context is useless
- how do agents create categories as needed or combine

Normalized database
- This type of data always goes into this field
- Vector DB has the articles and text
    - Break articles down by chunks of text to search from
- Foreign key for articles
    - Search for siamese cat
        - returns K-th results for siamese cats
        - only about 2 total links (keys) away, but want to know how strong they are
        - returns links
            - to siamese cat *articles*
            - cats category
                - points to cat in general articles

