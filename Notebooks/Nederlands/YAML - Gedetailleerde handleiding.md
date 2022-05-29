---
created: 2022-05-30T01:17:10 (UTC +02:00)
tags: []
source: https://www.tutorialspoint.com/yaml/yaml_quick_guide.htm?key=kubernetes
author: 
---

# YAML - Beknopte handleiding

> ## Excerpt
> YAML - Quick Guide,  YAML Ain't Markup Language is a data serialization language that matches userâs expectations about data. It designed to be human friendly and works perfect

---
___

  

## YAML - Inleiding

YAML Ain't Markup Language is een taal voor gegevensserialisatie die voldoet aan de verwachtingen van de gebruiker over gegevens. Het is ontworpen om mensvriendelijk te zijn en werkt perfect met andere programmeertalen. Het is handig om gegevens te beheren en bevat Unicode-afdrukbare tekens. Dit hoofdstuk geeft je een inleiding tot YAML en geeft je een idee over de functies ervan.

## Formatteren

Overweeg de onderstaande tekst −

```
Quick brown fox jumped over the lazy dog.

```

De YAML-tekst hiervoor wordt weergegeven zoals hieronder weergegeven −

```
yaml.load(Quick brown fox jumped over the lazy dog.)
>>'Quick brown fox jumped over the lazy dog.'
```

Merk op dat YAML de waarde in tekenreeksformaat neemt en de uitvoer vertegenwoordigt zoals hierboven vermeld.

## Voorbeelden

Laten we de formaten in YAML begrijpen met behulp van de volgende voorbeelden -

Overweeg het volgende puntnummer van "pi", dat een waarde heeft van 3,1415926. In YAML wordt het weergegeven als een drijvend getal zoals hieronder weergegeven −

```
>>> yaml.load('3.1415926536')
3.1415926536
```

Stel dat meerdere waarden moeten worden geladen in een specifieke gegevensstructuur zoals hieronder vermeld −

```
eggs
ham
spam
French basil salmon terrine

```

Wanneer u dit in YAML laadt, worden de waarden opgenomen in een arraygegevensstructuur die een vorm van lijst is. De uitvoer is zoals hieronder weergegeven −

```
>>> yaml.load('''
   - eggs
   - ham
   - spam
   - French basil salmon terrine
   ''')
['eggs', 'ham', 'spam', 'French basil salmon terrine']

```

## Functies

YAML bevat een opmaaktaal met een belangrijke constructie, om gegevensgeoriënteerde taal te onderscheiden van de documentopmaak. De ontwerpdoelen en kenmerken van YAML worden hieronder gegeven −

-   Komt overeen met native datastructuren van agile methodologie en zijn talen zoals Perl, Python, PHP, Ruby en JavaScript
    
-   YAML-gegevens zijn overdraagbaar tussen programmeertalen
    
-   Bevat gegevensconsistent gegevensmodel
    
-   Gemakkelijk leesbaar voor mensen
    
-   Ondersteunt verwerking in één richting
    
-   Eenvoudige implementatie en gebruik
    

## YAML - Basics

Now that you have an idea about YAML and its features, let us learn its basics with syntax and other operations. Remember that YAML includes a human readable structured format.

## Rules for Creating YAML file

When you are creating a file in YAML, you should remember the following basic rules −

-   YAML is case sensitive
    
-   The files should have **.yaml** as the extension
    
-   YAML does not allow the use of tabs while creating YAML files; spaces are allowed instead
    

## Basic Components of YAML File

The basic components of YAML are described below −

### Conventional Block Format

This block format uses **hyphen+space** to begin a new item in a specified list. Observe the example shown below −

```
--- # Favorite movies
 - Casablanca
 - North by Northwest
 - The Man Who Wasn't There

```

**Inline Format**

Inline format is delimited with **comma and space** and the items are enclosed in JSON. Observe the example shown below −

```
--- # Shopping list
   [milk, groceries, eggs, juice, fruits]

```

**Folded Text**

Folded text converts newlines to spaces and removes the leading whitespace. Observe the example shown below −

```
- {name: John Smith, age: 33}
- name: Mary Smith
  age: 27

```

The structure which follows all the basic conventions of YAML is shown below −

```
men: [John Smith, Bill Jones]
women:
  - Mary Smith
  - Susan Williams

```

## Synopsis of YAML Basic Elements

-   The synopsis of YAML basic elements is given here: Comments in YAML begins with the (**#**) character.
    
-   Comments must be separated from other tokens by whitespaces.
    
-   Indentation of whitespace is used to denote structure.
    
-   Tabs are not included as indentation for YAML files.
    
-   List members are denoted by a leading hyphen (**\-**).
    
-   List members are enclosed in square brackets and separated by commas.
    
-   Associative arrays are represented using colon **( : )** in the format of key value pair. They are enclosed in curly braces **{}**.
    
-   Multiple documents with single streams are separated with 3 hyphens (---).
    
-   Repeated nodes in each file are initially denoted by an ampersand (**&**) and by an asterisk (**\***) mark later.
    
-   YAML always requires colons and commas used as list separators followed by space with scalar values.
    
-   Nodes should be labelled with an exclamation mark (**!**) or double exclamation mark (**!!**), followed by string which can be expanded into an URI or URL.
    

## YAML - Indentation and Separation

Indentation and separation are two main concepts when you are learning any programming language. This chapter talks about these two concepts related to YAML in detail.

## Indentation of YAML

YAML does not include any mandatory spaces. Further, there is no need to be consistent. The valid YAML indentation is shown below −

```
a:
   b:
      - c
      -  d
      - e
f:
      "ghi"
```

-   You should remember the following rules while working with indentation in YAML:Flow blocks must be intended with at least some spaces with surrounding current block level.
    
-   Flow content of YAML spans multiple lines. The beginning of flow content begins with **{** or **\[**.
    
-   Block list items include same indentation as the surrounding block level because - is considered as a part of indentation.
    

### Example of Intended Block

Observe the following code that shows indentation with examples −

```
--- !clarkevans.com/^invoice
invoice: 34843
date   : 2001-01-23
bill-to: &id001
   given  : Chris
   family : Dumars
   address:
      lines: |
            458 Walkman Dr.
            Suite #292
      city    : Royal Oak
      state   : MI
      postal  : 48046
ship-to: *id001
product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
   - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
tax  : 251.42
total: 4443.52
comments: >
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338.
```

## Separation of Strings

Strings are separated using double-quoted string. If you escape the newline characters in a given string, it is completely removed and translated into space value.

### Example

In this example we have focused listing of animals listed as an array structure with data type of string. Every new element is listed with a prefix of hyphen as mentioned as prefix.

```
-
 - Cat
 - Dog
 - Goldfish
-
 - Python
 - Lion
 - Tiger

```

Another example to explain string representation in YAML is mentioned below.

```
 errors:
      messages:
         already_confirmed: "was already confirmed, please try signing in"
         confirmation_period_expired: "needs to be confirmed within %{period}, please request a new one"
         expired: "has expired, please request a new one"
         not_found: "not found"
         not_locked: "was not locked"
         not_saved:
            one: "1 error prohibited this %{resource} from being saved:"
            other: "%{count} errors prohibited this %{resource} from being saved:"

```

This example refers to the set of error messages which a user can use just by mentioning the key aspect and to fetch the values accordingly. This pattern of YAML follows the structure of JSON which can be understood by user who is new to YAML.

## YAML - Comments

Now that you are comfortable with the syntax and basics of YAML, let us proceed further into its details. In this chapter, we will see how to use comments in YAML.

**YAML supports single line comments**. Its structure is explained below with the help of an example −

```
# this is single line comment.

```

**YAML does not support multi line comments**. If you want to provide comments for multiple lines, you can do so as shown in the example below −

```
# this
# is a multiple
# line comment

```

## Features of Comments

The features of comments in YAML are given below −

-   A commented block is skipped during execution.
    
-   Comments help to add description for specified code block.
    
-   Comments must not appear inside scalars.
    
-   YAML does not include any way to escape the hash symbol (#) so within multi-line string so there is no way to divide the comment from the raw string value.
    

The comments within a collection are shown below −

```
key: #comment 1
   - value line 1
   #comment 2
   - value line 2
   #comment 3
   - value line 3

```

The shortcut key combination for commenting YAML blocks is **Ctrl+Q**.

If you are using **Sublime Text editor**, the steps for commenting the block are mentioned below −

Select the block. Use “CTRL + /” on Linux and Windows and “CMD+/” for Mac operating system. Execute the block.

Note that the same steps are applicable if you are using **Visual Studio Code Editor**. It is always recommended to use **Sublime Text Editor** for creating YAML files as it supported by most operating systems and includes developer friendly shortcut keys.

## YAML - Collections and Structures

YAML includes block collections which use indentation for scope. Here, each entry begins with a new line. Block sequences in collections indicate each entry with a **dash and space** (-). In YAML, block collections styles are not denoted by any specific indicator. Block collection in YAML can distinguished from other scalar quantities with an identification of key value pair included in them.

Mappings are the representation of key value as included in JSON structure. It is used often in multi-lingual support systems and creation of API in mobile applications. Mappings use key value pair representation with the usage of **colon and space** (**:**).

## Examples

Consider an example of sequence of scalars, for example a list of ball players as shown below −

```
- Mark Joseph
- James Stephen
- Ken Griffey

```

The following example shows mapping scalars to scalars −

```
hr: 87
avg: 0.298
rbi: 149

```

The following example shows mapping scalars to sequences −

```
European:
- Boston Red Sox
- Detroit Tigers
- New York Yankees

national:
- New York Mets
- Chicago Cubs
- Atlanta Braves

```

Collections can be used for sequence mappings which are shown below −

```
-
   name: Mark Joseph
   hr: 87
   avg: 0.278
-
   name: James Stephen
   hr: 63
   avg: 0.288

```

With collections, YAML includes flow styles using explicit indicators instead of using indentation to denote space. The flow sequence in collections is written as comma separated list enclosed in square brackets. The best illustration for collection which is included in PHP frameworks like symphony.

```
[PHP, Perl, Python]

```

These collections are stored in documents. The separation of documents in YAML is denoted with three hyphens or dashes (---). The end of document is marked with three dots (…).

The separation of documents in YAML is denoted by three dashes (---). The end of document is represented with three dots (…).

The document representation is referred as structure format which is mentioned below −

```
# Ranking of 1998 home runs
---
- Mark Joseph
- James Stephen
- Ken Griffey 

# Team ranking
---
- Chicago Cubs
- St Louis Cardinals

```

A question mark with a combination of space indicates a complex mapping in structure. Within a block collection, a user can include structure with a dash, colon and question mark. The following example shows the mapping between sequences −

```
- 2001-07-23
? [ New York Yankees,Atlanta Braves ]
: [ 2001-07-02, 2001-08-12, 2001-08-14]

```

## YAML - Scalars and Tags

Scalars in YAML are written in block format using a literal type which is denoted as(**|**). It denotes line breaks count. In YAML, scalars are written in folded style (**\>**) where each line denotes a folded space which ends with an **empty line** or **more indented** line.

New lines are preserved in literals are shown below −

```
ASCII Art
--- |
\//||\/||
// || ||__

```

The folded newlines are preserved for **more indented lines** and **blank lines** as shown below −

```
>
Sammy Sosa completed another
fine season with great stats.
63 Home Runs
0.288 Batting Average
What a year!
```

YAML flow scalars include plain styles and quoted styles. The double quoted style includes various escape sequences. Flow scalars can include multiple lines; line breaks are always folded in this structure.

```
plain:
This unquoted scalar
spans many lines.
quoted: "So does this
quoted scalar.\n"

```

In YAML, untagged nodes are specified with a specific type of the application. The examples of tags specification generally use **seq, map** and **str** types for YAML tag repository. The tags are represented as examples which are mentioned as below −

## Integer tags

These tags include integer values in them. They are also called as numeric tags.

```
canonical: 12345
decimal: +12,345
sexagecimal: 3:25:45
octal: 014
hexadecimal: 0xC

```

## Floating point numbers

These tags include decimal and exponential values. They are also called as exponential tags.

```
canonical: 1.23015e+3
exponential: 12.3015e+02
sexagecimal: 20:30.15
fixed: 1,230.15
negative infinity: -.inf
not a number: .NaN

```

## Miscellaneous Tags

It includes a variety of integer, floating and string values embedded in them. Hence it is called miscellaneous tags.

```
null: ~
true: y
false: n
string: '12345'

```

## YAML - Full Length Example

The following full-length example specifies the construct of YAML which includes symbols and various representations which will be helpful while converting or processing them in JSON format. These attributes are also called as key names in JSON documents. These notations are created for security purposes.

The above YAML format represents various attributes of defaults, adapter, and host with various other attributes. YAML also keeps a log of every file generated which maintains a track of error messages generated. On converting the specified YAML file in JSON format we get a desired output as mentioned below −

```
defaults: &defaults
   adapter:  postgres
   host:     localhost

development:
   database: myapp_development
   <<: *defaults

test:
   database: myapp_test
   <<: *defaults
```

Let’s convert the YAML to JSON format and check on the output.

```
{
   "defaults": {
      "adapter": "postgres",
      "host": "localhost"
   },
   "development": {
      "database": "myapp_development",
      "adapter": "postgres",
      "host": "localhost"
   },
   "test": {
      "database": "myapp_test",
      "adapter": "postgres",
      "host": "localhost"
   }
}
```

The defaults key with a prefix of “ <<: \*” is included as and when required with no need to write the same code snippet repeatedly.

## YAML - Processes

YAML follows a standard procedure for Process flow. The native data structure in YAML includes simple representations such as nodes. It is also called as Representation Node Graph.

It includes mapping, sequence and scalar quantities which is being serialized to create a serialization tree. With serialization the objects are converted with stream of bytes.

The serialization event tree helps in creating presentation of character streams as represented in the following diagram.

The reverse procedure parses the stream of bytes into serialized event tree. Later, the nodes are converted into node graph. These values are later converted in YAML native data structure. The figure below explains this −

![YAML Processes](data:image/jpeg;base64,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6WG2NpFcXflqv+rMduZNxUbMKQD2X42/Hfwb+zb8OL/xd498TaN4S8N6aoM9/qdysEQYnCxrnl5HbCpGgLuxCqCxAr5hl8J+Pf8AgqpNH/wl2h6/8Lf2bi6yHw1qcTWXif4kqrHjUI879P0xiB/op/0i4XHmmKNjE/oHwW/4Jt+FfBfxI074h/EHXvEnxq+KunAPa+J/F8kciaPIVw/9m2ESpZ6epJOPJiEmCA8rkZP0XQBX0nSbXQNKtrGxtreysrKJILe3gjEcUEagKqIowFUAAAAYAFWKKKACiiigAooooAKKKKACiiigAooooAKKKKAPn/8A4Kxf8osv2lv+yVeKP/TRdUUf8FYv+UWX7S3/AGSrxR/6aLqigA/4JO/8osv2af8AslXhf/00WtfQFfP/APwSd/5RZfs0/wDZKvC//pota+gKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArhv2eh4pXwFf/APCYa5pPiLVv+Em18291pxQwxaf/AGze/wBn2rbEQebb2X2aCXgt5sMm5nbLt3NeL/sGX+iaj8D9ck8P6de6XYL8RfHMUsN3di6ke7Txbq6XcwcImEluVmkRMExpIqFnK72APaKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAMnwL4G0n4aeENP0DQrGLTdH0mEW9paxZ2QRjooyScCtaiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAPn/AP4Kxf8AKLL9pb/slXij/wBNF1RR/wAFYv8AlFl+0t/2SrxR/wCmi6ooAP8Agk7/AMosv2af+yVeF/8A00WtfQFfP/8AwSd/5RZfs0/9kq8L/wDpota+gKACiiigAooooAKKKKAPzm/4Lk/8F3NY/wCCTeiRaf4e+DHi7xbrWqRqLTxJqdq9r4RtJHUlVa5TLzzKcZgXysgn96CMV+QH7Hv/AAdufGr4OftDeM/HvxZ0i9+L8PiXTYNP0zw7a+If+Ed0fw75chdpIbdbadGdwQpdh5mBy7DAH9RHirwppfjrw3e6Nrem2GsaRqcLW95Y31ulxbXcTDDJJG4KupHUEEGvnf8AZA/4JJ/Bb9gr9oTxp8QvhNoFx4Pn8e6fDYan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)

The information in YAML is used in two ways: **machine processing** and **human consumption**. The processor in YAML is used as a tool for the procedure of converting information between complementary views in the diagram given above. This chapter describes the information structures a YAML processor must provide within a given application.

YAML includes a serialization procedure for representing data objects in serial format. The processing of YAML information includes three stages: **Representation, Serialization, Presentation and parsing**. Let us discuss each of them in detail.

## Representation

YAML represents the data structure using three kinds of nodes: **sequence, mapping** and **scalar**.

### Sequence

Sequence refers to the ordered number of entries, which maps the unordered association of key value pair. It corresponds to the Perl or Python array list.

The code shown below is an example of sequence representation −

```
product:
   - sku         : BL394D
     quantity    : 4
     description : Football
     price       : 450.00
   - sku         : BL4438H
     quantity    : 1
     description : Super Hoop
     price       : 2392.00
```

### Mapping

Mapping on the other hand represents dictionary data structure or hash table. An example for the same is mentioned below −

```
batchLimit: 1000
threadCountLimit: 2
key: value
keyMapping: <What goes here?>

```

### Scalars

Scalars represent standard values of strings, integers, dates and atomic data types. Note that YAML also includes nodes which specify the data type structure. For more information on scalars, please refer to the chapter 6 of this tutorial.

## Serialization

Serialization process is required in YAML that eases human friendly key order and anchor names. The result of serialization is a YAML serialization tree. It can be traversed to produce a series of event calls of YAML data.

An example for serialization is given below −

```
consumer:
   class: 'AppBundle\Entity\consumer'
   attributes:
      filters: ['customer.search', 'customer.order', 'customer.boolean']
   collectionOperations:
      get:
         method: 'GET'
         normalization_context:
       groups: ['customer_list']
   itemOperations:
      get:
         method: 'GET'
         normalization_context:
            groups: ['customer_get']

```

## Presentation

The final output of YAML serialization is called presentation. It represents a character stream in a human friendly manner. YAML processor includes various presentation details for creating stream, handling indentation and formatting content. This complete process is guided by the preferences of user.

An example for YAML presentation process is the result of JSON value created. Observe the code given below for a better understanding −

```
{
   "consumer": {
      "class": "AppBundle\\Entity\\consumer",
      "attributes": {
         "filters": [
            "customer.search",
            "customer.order",
            "customer.boolean"
         ]
      },
      "collectionOperations": {
         "get": {
            "method": "GET",
            "normalization_context": {
               "groups": [
                  "customer_list"
               ]
            }
         }
      },
      "itemOperations": {
         "get": {
            "method": "GET",
            "normalization_context": {
               "groups": [
                  "customer_get"
               ]
            }
         }
      }
   }
}
```

## Parsing

Parsing is the inverse process of presentation; it includes a stream of characters and creates a series of events. It discards the details introduced in the presentation process which causes serialization events. Parsing procedure can fail due to ill-formed input. It is basically a procedure to check whether YAML is well-formed or not.

Consider a YAML example which is mentioned below −

```
---
   environment: production
   classes:
      nfs::server:
         exports:
            - /srv/share1
            - /srv/share3
   parameters:
      paramter1
```

With three hyphens, it represents the start of document with various attributes later defined in it.

YAML lint is the online parser of YAML and helps in parsing the YAML structure to check whether it is valid or not. The official link for YAML lint is mentioned below: [http://www.yamllint.com/](http://www.yamllint.com/)

You can see the output of parsing as shown below −

![YAML Lint](data:image/jpeg;base64,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)

## YAML - Information Models

This chapter will explain the detail about the procedures and processes that we discussed in last chapter. Information Models in YAML will specify the features of serialization and presentation procedure in a systematic format using a specific diagram.

For an information model, it is important to represent the application information which are portable between programming environments.

![YAML Information Models](data:image/jpeg;base64,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)

The diagram shown above represents a normal information model which is represented in graph format. In YAML, the representation of native data is rooted, connected and is directed graph of tagged nodes. If we mention directed graph, it includes a set of nodes with directed graph. As mentioned in the information model, YAML supports three kinds of nodes namely −

-   Sequences
-   Scalars
-   Mappings

The basic definitions of these representation nodes were discussed in last chapter. In this chapter, we will focus on schematic view of these terms. The following sequence diagram represents the workflow of legends with various types of tags and mapping nodes.

![Sequence Diagram Workflow of Legends](data:image/jpeg;base64,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)

There are three types of nodes: **sequence node, scalar node** and **mapping node**.

### Sequences

Sequence node follows a sequential architecture and includes an ordered series of zero or more nodes. A YAML sequence may contain the same node repeatedly or a single node.

### Scalars

The content of scalars in YAML includes Unicode characters which can be represented in the format with a series of zero. In general, scalar node includes scalar quantities.

### Mapping

Mapping node includes the key value pair representation. The content of mapping node includes a combination of key-value pair with a mandatory condition that key name should be maintained unique. Sequences and mappings collectively form a collection.

Note that as represented in the diagram shown above, scalars, sequences and mappings are represented in a systematic format.

## YAML - Syntax Characters

Various types of characters are used for various functionalities. This chapter talks in detail about syntax used in YAML and focuses on character manipulation.

## Indicator Characters

Indicator characters include a special semantics used to describe the content of YAML document. The following table shows this in detail.

| Sr.No. | Character & Functionality |
| --- | --- |
| 1 | 
**\_**

It denotes a block sequence entry

 |
| 2 | 

**?**

It denotes a mapping key

 |
| 3 | 

**:**

It denotes a mapping value

 |
| 4 | 

**,**

It denotes flow collection entry

 |
| 5 | 

**\[**

It starts a flow sequence

 |
| 6 | 

**\]**

It ends a flow sequence

 |
| 7 | 

**{**

It starts a flow mapping

 |
| 8 | 

**}**

It ends a flow mapping

 |
| 9 | 

**#**

It denotes the comments

 |
| 10 | 

**&**

It denotes node’s anchor property

 |
| 11 | 

**\***

It denotes alias node

 |
| 12 | 

**!**

It denotes node’s tag

 |
| 13 | 

**|**

It denotes a literal block scalar

 |
| 14 | 

**\>**

It denotes a folded block scalar

 |
| 15 | 

**\`**

Single quote surrounds a quoted flow scalar

 |
| 16 | 

**"**

Double quote surrounds double quoted flow scalar

 |
| 17 | 

**%**

It denotes the directive used

 |

The following example shows the characters used in syntax −

```
%YAML 1.1
---
!!map {
   ? !!str "sequence"
   : !!seq [
      !!str "one", !!str "two"
   ],
   ? !!str "mapping"
   : !!map {
      ? !!str "sky" : !!str "blue",
      ? !!str "sea" : !!str "green",
   }
}

# This represents
# only comments.
---
!!map1 {
   ? !!str "anchored"
   : !local &A1 "value",
   ? !!str "alias"
   : *A1,
}
!!str "text"
```

## YAML - Syntax Primitives

In this chapter you will learn about the following aspects of syntax primitives in YAML −

-   Production parameters
-   Indentation Spaces
-   Separation Spaces
-   Ignored Line Prefix
-   Line folding

Let us understand each aspect in detail.

## Production Parameters

Production parameters include a set of parameters and the range of allowed values which are used on a specific production. The following list of production parameters are used in YAML −

### Indentation

It is denoted by character **n** or **m** Character stream depends on the indentation level of blocks included in it. Many productions have parameterized these features.

### Context

It is denoted by **c**. YAML supports two groups of contexts: **block styles** and **flow styles**.

### Style

It is denoted by s. Scalar content may be presented in one of the five styles: **plain, double quoted and single quoted flow, literal and folded block.**

### Chomping

It is denoted by **t**. Block scalars offer many mechanisms which help in trimming the block: **strip, clip** and **keep**. Chomping helps in formatting new line strings. It is used Block style representation. Chomping process happens with the help of indicators. The indicators controls what output should be produced with newlines of string. The newlines are removed with **(-)** operator and newlines are added with **(+)** operator.

An example for chomping process is shown below −

```
strip: |-
   text↓
clip: |
   text↓
keep: |+
   text↓

```

The output after parsing the specified YAML example is as follows −

![Output After Parsing the Specified YAML](data:image/jpeg;base64,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)

## Indentation Spaces

In YAML character stream, indentation is defined as a line break character by zero or more characters. The most important point to be kept in mind is that indentation must not contain any tab characters. The characters in indentation should never be considered as a part of node’s content information. Observe the following code for better understanding −

```
%YAML 1.1
---
!!map {
   ? !!str "Not indented"
   : !!map {
      ? !!str "By one space"
      : !!str "By four\n spaces\n",
      ? !!str "Flow style"
      : !!seq [
         !!str "By two",
         !!str "Still by two",
         !!str "Again by two",
      ]
   }
}
```

The output that you can see after indentation is as follows −

```
{
   "Not indented": {
      "By one space": "By four\n spaces\n", 
      "Flow style": [
         "By two", 
         "Still by two", 
         "Again by two"
      ]
   }
}

```

## Separation Spaces

YAML uses space characters for separation between tokens. The most important note is that separation in YAML should not contain tab characters.

The following lone of code shows the usage of separation spaces −

```
{ · first: · Sammy, · last: · Sosa · }
```

The syntax shown above gives you the following output:

```
{
   "\u00b7 last": "\u00b7 Sosa \u00b7", 
   "\u00b7 first": "\u00b7 Sammy"
}

```

## Ignored Line Prefix

Empty prefix always includes indentation depending on the scalar type which also includes a leading whitespace. Plain scalars should not contain any tab characters. On the other hand, quoted scalars may contain tab characters. Block scalars completely depend on indentation.

The following example shows the working of ignored line prefix in a systematic manner −

```
%YAML 1.1
---
!!map {
   ? !!str "plain"
   : !!str "text lines",
   ? !!str "quoted"
   : !!str "text lines",
   ? !!str "block"
   : !!str "text·®lines\n"
}
```

The output achieved for the block streams is as follows −

```
{
   "plain": "text lines", 
   "quoted": "text lines", 
   "block": "text\u00b7\u00aelines\n"
}

```

## Line Folding

Line Folding allows breaking long lines for readability. More amounts of short lines mean better readability. Line folding is achieved by noting original semantics of long line. The following example demonstrates line folding −

```
%YAML 1.1
--- !!str
"specific\L\
trimmed\n\n\n\
as space"
```

You can see the output for line folding in JSON format as follows −

```
"specific\u2028trimmed\n\n\nas space"

```

## YAML - Character Streams

In YAML, you come across various character streams as follows −

-   Directives
-   Document Boundary Markers
-   Documents
-   Complete Stream

In this chapter, we will discuss them in detail.

## Directives

Directives are basic instructions used in YAML processor. Directives are the presentation details like comments which are not reflected in serialization tree. In YAML, there is no way to define private directives. This section discusses various types of directives with relevant examples −

### Reserved Directives

Reserved directives are initialized with three hyphen characters (---) as shown in the example below. The reserved directives are converted into specific value of JSON.

```
%YAML 1.1
--- !!str
"foo"

```

### YAML Directive

YAML Directives are default directives. If converted in JSON, the value fetched includes forward slash character in preceding and terminating characters.

```
%YAML 1.1
---
!!str "foo"

```

## Document Boundary Markers

YAML uses these markers to allow more than one document to be contained in one stream. These markers are specially used to convey the structure of YAML document. Note that a line beginning with “---“is used to start a new document.

The following code explains about this with examples −

```
%YAML 1.1
---
!!str "foo"
%YAML 1.1
---
!!str "bar"
%YAML 1.1
---
!!str "baz"

```

## Documents

YAML document is considered as a single native data structure presented as a single root node. The presentation details in YAML document such as directives, comments, indentation and styles are not considered as contents included in them.

There are two types of documents used in YAML. They are explained in this section −

### Explicit Documents

It begins with the document start marker followed by the presentation of the root node. The example of YAML explicit declaration is given below −

```
---

some: yaml

...

```

It includes an explicit start and end markers which is “---“and “…” in given example. On converting the specified YAML in JSON format, we get the output as shown below −

```
{
   "some": "yaml"
}

```

### Implicit Documents

These documents do not begin with a document start marker. Observe the code given below −

```
fruits:
   - Apple
   - Orange
   - Pineapple
   - Mango

```

Converting these values in JSON format we get the output as a simple JSON object as given below −

```
{
   "fruits": [
      "Apple",
      "Orange",
      "Pineapple",
      "Mango"
   ]
}

```

## Complete Stream

YAML includes a sequence of bytes called as character stream. The stream begins with a prefix containing a byte order denoting a character encoding. The complete stream begins with a prefix containing a character encoding, followed by comments.

An example of complete stream (character stream) is shown below −

```
%YAML 1.1
---
!!str "Text content\n"

```

## YAML - Node Properties

Each presentation node includes two major characteristics called **anchor** and **tag**. Node properties may be specified with node content, omitted from the character stream.

The basic example of node representation is as follows −

```
%YAML 1.1
---
!!map {
   ? &A1 !!str "foo"
   : !!str "bar",
   ? !!str &A2 "baz"
   : *a1
}

```

## Node Anchors

The anchor property represents a node for future reference. The character stream of YAML representation in node is denoted with the **ampersand (&)** indicator. The YAML processor need not preserve the anchor name with the representation details composed in it. The following code explains this −

```
%YAML 1.1
---
!!map {
   ? !!str "First occurence"
   : &A !!str "Value",
   ? !!str "Second occurence"
   : *A
}
```

The output of YAML generated with anchor nodes is shown below −

```
---
!!map {
   ? !!str "First occurence"
   : !!str "Value",
   ? !!str "Second occurence"
   : !!str "Value",
}

```

## Node Tags

The tag property represents the type of native data structure which defines a node completely. A tag is represented with the (**!**) indicator. Tags are considered as an inherent part of the representation graph. The following example of explains node tags in detail −

```
%YAML 1.1
---
!!map {
   ? !<tag:yaml.org,2002:str> "foo"
   : !<!bar> "baz"
}
```

## Node Content

Node content can be represented in a flow content or block format. Block content extends to the end of line and uses indentation to denote structure. Each collection kind can be represented in a specific single flow collection style or can be considered as a single block. The following code explains this in detail −

```
%YAML 1.1
---
!!map {
   ? !!str "foo"
   : !!str "bar baz"
}

%YAML 1.1
---
!!str "foo bar"

%YAML 1.1
---
!!str "foo bar"

%YAML 1.1
---
!!str "foo bar\n"
```

## YAML - Block Scalar Header

In this chapter, we will focus on various scalar types which are used for representing the content. In YAML, comments may either precede or follow scalar content. It is important to note that comments should not be included within scalar content.

Note that all flow scalar styles can include multiple lines, except with usage in multiple keys.

The representation of scalars is given below −

```
%YAML 1.1
---
!!map {
   ? !!str "simple key"
   : !!map {
      ? !!str "also simple"
      : !!str "value",
      ? !!str "not a simple key"
      : !!str "any value"
   }
}
```

The generated output of block scalar headers is shown below −

```
{
   "simple key": {
      "not a simple key": "any value", 
      "also simple": "value"
   }
}
```

## Document Marker Scalar Content

All characters in this example are considered as content, including the inner space characters.

```
%YAML 1.1
---
!!map {
   ? !!str "---"
   : !!str "foo",
   ? !!str "...",
   : !!str "bar"
}

%YAML 1.1
---
!!seq [
   !!str "---",
   !!str "...",
   !!map {
      ? !!str "---"
      : !!str "..."
   }
]
```

The plain line breaks are represented with the example given below −

```
%YAML 1.1
---
!!str "as space \
trimmed\n\
specific\L\n\
none"
```

The corresponding JSON output for the same is mentioned below −

```
"as space trimmed\nspecific\u2028\nnone"

```

## YAML - Flow Styles

Flow styles in YAML can be thought of as a natural extension of JSON to cover the folding content lines for better readable feature which uses anchors and aliases to create the object instances. In this chapter, we will focus on flow representation of the following concepts −

-   Alias Nodes
-   Empty Nodes
-   Flow Scalar styles
-   Flow collection styles
-   Flow nodes

The example of alias nodes is shown below −

```
%YAML 1.2
---
!!map {
   ? !!str "First occurrence"
   : &A !!str "Foo",
   ? !!str "Override anchor"
   : &B !!str "Bar",
   ? !!str "Second occurrence"
   : *A,
   ? !!str "Reuse anchor"
   : *B,
}
```

The JSON output of the code given above is given below −

```
{
   "First occurrence": "Foo", 
   "Second occurrence": "Foo", 
   "Override anchor": "Bar", 
   "Reuse anchor": "Bar"
}

```

Nodes with empty content are considered as empty nodes. The following example shows this −

```
%YAML 1.2
---
!!map {
   ? !!str "foo" : !!str "",
   ? !!str "" : !!str "bar",
}
```

The output of empty nodes in JSON is represented as below −

```
{
   "": "bar", 
   "foo": ""
}

```

Flow scalar styles include double-quoted, single-quoted and plain types. The basic example for the same is given below −

```
%YAML 1.2
---
!!map {
   ? !!str "implicit block key"
   : !!seq [
      !!map {
         ? !!str "implicit flow key"
         : !!str "value",
      }
   ]  
}
```

The output in JSON format for the example given above is shown below −

```
{
   "implicit block key": [
      {
         "implicit flow key": "value"
      }
   ] 
}

```

Flow collection in YAML is nested with a block collection within another flow collection. Flow collection entries are terminated with **comma** (**,**) indicator. The following example explains the flow collection block in detail −

```
%YAML 1.2
---
!!seq [
   !!seq [
      !!str "one",
      !!str "two",
   ],
   
   !!seq [
      !!str "three",
      !!str "four",
   ],
]
```

The output for flow collection in JSON is shown below −

```
[
   [
      "one", 
      "two"
   ], 
   [
      "three", 
      "four"
   ]
]

```

Flow styles like JSON include start and end indicators. The only flow style that does not have any property is the plain scalar.

```
%YAML 1.2
---
!!seq [
!!seq [ !!str "a", !!str "b" ],
!!map { ? !!str "a" : !!str "b" },
!!str "a",
!!str "b",
!!str "c",]
```

The output for the code shown above in JSON format is given below −

```
[
   [
      "a", 
      "b"
   ], 
   
   {
      "a": "b"
   }, 
   
   "a", 
   "b", 
   "c"
]

```

## YAML - Block Styles

YAML includes two block scalar styles: **literal** and **folded**. Block scalars are controlled with few indicators with a header preceding the content itself. An example of block scalar headers is given below −

```
%YAML 1.2
---
!!seq [
   !!str "literal\n",
   !!str "·folded\n",
   !!str "keep\n\n",
   !!str "·strip",
]
```

The output in JSON format with a default behavior is given below −

```
[
   "literal\n", 
   "\u00b7folded\n", 
   "keep\n\n", 
   "\u00b7strip"
]

```

## Types of Block Styles

There are four types of block styles: **literal, folded, keep** and **strip** styles. These block styles are defined with the help of Block Chomping scenario. An example of block chomping scenario is given below −

```
%YAML 1.2
---
!!map {
   ? !!str "strip"
   : !!str "# text",
   ? !!str "clip"
   : !!str "# text\n",
   ? !!str "keep"
   : !!str "# text\n",
}

```

You can see the output generated with three formats in JSON as given below −

```
{
   "strip": "# text", 
   "clip": "# text\n", 
   "keep": "# text\n"
}

```

Chomping in YAML controls the final breaks and trailing empty lines which are interpreted in various forms.

### Stripping

In this case, the final line break and empty lines are excluded for scalar content. It is specified by the chomping indicator “-“.

### Clipping

Clipping is considered as a default behavior if no explicit chomping indicator is specified. The final break character is preserved in the scalar’s content. The best example of clipping is demonstrated in the example above. It terminates with newline **“\\n”** character.

### Keeping

Keeping refers to the addition with representation of “+” chomping indicator. Additional lines created are not subject to folding. The additional lines are not subject to folding.

## YAML - Sequence Styles

To understand sequence styles, it is important to understand collections. The concept of collections and sequence styles work in parallel. The collection in YAML is represented with proper sequence styles. If you want to refer proper sequencing of tags, always refer to collections. Collections in YAML are indexed by sequential integers starting with zero as represented in arrays. The focus of sequence styles begins with collections.

## Example

Let us consider the number of planets in universe as a sequence which can be created as a collection. The following code shows how to represent the sequence styles of planets in universe −

```
# Ordered sequence of nodes in YAML STRUCTURE
Block style: !!seq
- Mercury   # Rotates - no light/dark sides.
- Venus     # Deadliest. Aptly named.
- Earth     # Mostly dirt.
- Mars      # Seems empty.
- Jupiter   # The king.
- Saturn    # Pretty.
- Uranus    # Where the sun hardly shines.
- Neptune   # Boring. No rings.
- Pluto     # You call this a planet?
Flow style: !!seq [ Mercury, Venus, Earth, Mars,      # Rocks
                    Jupiter, Saturn, Uranus, Neptune, # Gas
                    Pluto ]                           # Overrated
```

Then, you can see the following output for ordered sequence in JSON format −

```
{
   "Flow style": [
      "Mercury", 
      "Venus", 
      "Earth", 
      "Mars", 
      "Jupiter", 
      "Saturn", 
      "Uranus", 
      "Neptune", 
      "Pluto"
   ], 
   
   "Block style": [
      "Mercury", 
      "Venus", 
      "Earth", 
      "Mars", 
      "Jupiter", 
      "Saturn", 
      "Uranus", 
      "Neptune", 
      "Pluto"
   ]
}

```

## YAML - Flow Mappings

Flow mappings in YAML represent the unordered collection of key value pairs. They are also called as mapping node. Note that keys should be maintained unique. If there is a duplication of keys in flow mapping structure, it will generate an error. The key order is generated in serialization tree.

## Example

An example of flow mapping structure is shown below −

```
%YAML 1.1
paper:
   uuid: 8a8cbf60-e067-11e3-8b68-0800200c9a66
   name: On formally undecidable propositions of  Principia Mathematica and related systems I.
   author: Kurt Gödel.
tags:
   - tag:
      uuid: 98fb0d90-e067-11e3-8b68-0800200c9a66
      name: Mathematics
   - tag:
      uuid: 3f25f680-e068-11e3-8b68-0800200c9a66
      name: Logic
```

The output of mapped sequence (unordered list) in JSON format is as shown below −

```
{
   "paper": {
      "uuid": "8a8cbf60-e067-11e3-8b68-0800200c9a66",
      "name": "On formally undecidable propositions of Principia Mathematica and related systems I.",
      "author": "Kurt Gödel."
   },
   "tags": [
      {
         "tag": {
            "uuid": "98fb0d90-e067-11e3-8b68-0800200c9a66",
            "name": "Mathematics"
         }
      },
      {
         "tag": {
            "uuid": "3f25f680-e068-11e3-8b68-0800200c9a66",
            "name": "Logic"
         }
      }
   ]
}

```

If you observe this output as shown above, it is observed that the key names are maintained unique in YAML mapping structure.

## YAML - Block Sequences

The block sequences of YAML represent a series of nodes. Each item is denoted by a leading “-“ indicator. Note that the “-“ indicator in YAML should be separated from the node with a white space.

The basic representation of block sequence is given below −

```
block sequence:
··- one↓
  - two : three↓

```

## Example

Observe the following examples for a better understanding of block sequences.

### Example 1

```
port: &ports
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  <<: *ports
```

The output of block sequences in JSON format is given below −

```
{
   "port": {
      "adapter": "postgres",
      "host": "localhost"
   },
   "development": {
      "database": "myapp_development",
      "adapter": "postgres",
      "host": "localhost"
   }
}

```

## YAML - Failsafe Schema

A YAML schema is defined as a combination of set of tags and includes a mechanism for resolving non-specific tags. The failsafe schema in YAML is created in such a manner that it can be used with any YAML document. It is also considered as a recommended schema for a generic YAML document.

## Types

There are two types of failsafe schema: **Generic Mapping** and **Generic Sequence**

### Generic Mapping

It represents an associative container. Here, each key is unique in the association and mapped to exactly one value. YAML includes no restrictions for key definitions.

An example for representing generic mapping is given below −

```
Clark : Evans
Ingy : döt Net
Oren : Ben-Kiki
Flow style: !!map { Clark: Evans, Ingy: döt Net, Oren: Ben-Kiki }
```

The output of generic mapping structure in JSON format is shown below −

```
{
   "Oren": "Ben-Kiki", 
   "Ingy": "d\u00f6t Net", 
   "Clark": "Evans", 
   "Flow style": {
      "Oren": "Ben-Kiki", 
      "Ingy": "d\u00f6t Net", 
      "Clark": "Evans"
   }
}

```

### Generic Sequence

It represents a type of sequence. It includes a collection indexed by sequential integers starting with zero. It is represented with **!!seq** tag.

```
Clark : Evans
Ingy : döt Net
Oren : Ben-Kiki
Flow style: !!seq { Clark: Evans, Ingy: döt Net, Oren: Ben-Kiki }
```

The output for this generic sequence of failsafe

```
schema is shown below:
{
   "Oren": "Ben-Kiki", 
   "Ingy": "d\u00f6t Net", 
   "Clark": "Evans", 
   "Flow style": {
      "Oren": "Ben-Kiki", 
      "Ingy": "d\u00f6t Net", 
      "Clark": "Evans"
   }
}
```

## YAML - JSON Schema

JSON schema in YAML is considered as the common denominator of most modern computer languages. It allows parsing JSON files. It is strongly recommended in YAML that other schemas should be considered on JSON schema. The primary reason for this is that it includes key value combination which are user friendly. The messages can be encoded as key and can be used as and when needed.

The JSON schema is scalar and lacks a value. A mapping entry in JSON schema is represented in the format of some key and value pair where null is treated as valid.

## Example

A null JSON schema is represented as shown below −

```
!!null null: value for null key
key with null value: !!null null
```

The output of JSON representation is mentioned below −

```
{
   "null": "value for null key", 
   "key with null value": null
}

```

### Example

The following example represents the Boolean JSON schema −

```
YAML is a superset of JSON: !!bool true
Pluto is a planet: !!bool false
```

The following is the output for the same in JSON format −

```
{
   "YAML is a superset of JSON": true, 
   "Pluto is a planet": false
}

```

### Example

The following example represents the integer JSON schema −

```
negative: !!int -12
zero: !!int 0
positive: !!int 34

```

The output of integer generated JSON schema is shown below:

```
{
   "positive": 34, 
   "zero": 0, 
   "negative": -12
}

```

### Example

The tags in JSON schema is represented with following example −

```
A null: null
Booleans: [ true, false ]
Integers: [ 0, -0, 3, -19 ]
Floats: [ 0., -0.0, 12e03, -2E+05 ]
Invalid: [ True, Null, 0o7, 0x3A, +12.3 ]
```

You can find the JSON Output as shown below −

```
{
   "Integers": [
      0, 
      0, 
      3, 
      -19
   ], 
   
   "Booleans": [
      true, 
      false
   ], 
   "A null": null, 

   "Invalid": [
         true, 
         null, 
         "0o7", 
         58, 
         12.300000000000001
   ], 
   
   "Floats": [
      0.0, 
      -0.0, 
      "12e03", 
      "-2E+05"
   ]
}

```
