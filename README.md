Health Vocabulary REST API
==========================

A swiss-army knife for all health/biomedical terminology/vocabulary related functions. Perform terminology queries on SNOMED-CT, LOINC, RXNORM or any of the 160 vocabularies in the [Unified Medical Language System](http://www.nlm.nih.gov/research/umls/). (Note: a separate download/license is required from the [NLM site](https://uts.nlm.nih.gov//license.html) to use this tool) 

Here is a [Demo Site](http://vocabapi.appliedinformaticsinc.com/demo)

API operations
--------------

**GET /code/**&lt;vocab&gt;/&lt;code_val&gt;

Get the full display name of a code for a given vocab

*Parameters:*

  - **vocab**: The vocabularly abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available [here](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/source_vocabularies.html)
  - **code_val**: The value of code to be looked up, e.g. 111-ABC


Sample Query:

* * *

**GET /rel/**&lt;vocab&gt;/&lt;code_val&gt;/&lt;rel_type&gt;

Get all target codes related to a given vocab/code pair by relationship rel_type

*Parameters:*

  - **vocab**: The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available [here](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/source_vocabularies.html)
  - **code_val**: The value of code to be looked up, e.g. 111-ABC
  - **rel_type**: The relationship to be looked up, e.g. is_diagnosed_by, causative_agent_of. The full list of rel_type abbreviations are available [here](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html)

* * *

**GET /map/**&lt;source_vocab&gt;/&lt;code_val&gt;/&lt;target_vocab&gt;

Get a "semantically equivalent" code in target vocabulary for a given code_val in source vocabulary

*Parameters:*

  - **source_vocab**, **target_vocab**: The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available [here](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/source_vocabularies.html)
  - **code_val**: The value of code to be looked up, e.g. 111-ABC


* * *
Requirements
------------

- Python 2.7
- Django 1.4 or above
- MySQL or any other relational database supported by Django
- [UMLS Metathesaurus](http://www.nlm.nih.gov/research/umls/) Files in .SQL format.

* * *
Install/Set up
--------------

1. Check out the code into your local. 
2. Edit *settings.py( and update DATABASE settings to point to your local database
3. Create corresponding database tables, *python manage.py syncdb*
4. Load the MRCONSO.sql and MRREL.sql (pronounced as Mr. Conso, Mr. Rel) into database from command line as follows: 

  mysql -u&lt;user&gt; -p&lt;password&gt; &lt;db_name&gt; &lt; MRCONSO.sql
 
  alter table MRCONSO add column id int auto_increment primary key;

  mysql -u&lt;user&gt; -p&lt;password&gt; &lt;db_name&gt; &lt; MRREL.sql
  
  alter table MRREL add column id int auto_increment primary key;
  
5. Run the app, python manage.py runserver
6. For production environment, it is advised to host the app inside a [WSGI](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/) container.


TODOs
-----

- Currently, it does not have authentication or rate throttling mechanism. The API is currently designed for internal apps consumption. 
- Develop a commands.py to load the UMLS files into the database instead of load into local
- A memcached version to store the tables in memory instead of a relational database
- Create a fully expanded ISA hierarcy to support class based queries

Frequently Asked Questions
--------------------------
* Why did you create this API?

  It was one of late spring days in NYC, we were coding our patient portal app for the New York eHealth Collaborative Challenge. They provided us with oh-so-[SHIN-NY](http://digitalhealthaccelerator.com/shiny-api/) API, but it sent us raw CCDA files and we wanted to display patient friendly lab result names. So we coded up this API that was called by our Javascript client on the patient portal to display nicer lab names.

* How is it different from the [UMLS Terminology Services](https://uts.nlm.nih.gov/home.html)?

   Our goal with Health Vocabulary REST API was to create a developer friendly API that abstracts-away a lot of UMLS specific notions to support rapid app development. The UTS provides a full-fledged web services based interface. Additionally, this API server can be hosted and managed locally.

* Can I get support to get this API set up for us?

  Absolutely! Just shoot us an email at info@appliedinformaticsinc.com 


* * *

LICENSE
-------
Copyright (c) 2013 by Applied Informatics Inc. Licensed under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) license.
