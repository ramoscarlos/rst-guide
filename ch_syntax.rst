Basic Syntax
============



This chapter covers what you need to know to get started using reST in your daily life, and is intended to serve as a reference in case you forget how to do something in particular.



Paragraphs and whitespace
-------------------------



To write a paragraph, just type, without any special indicators. However, before creating a second paragraph, is necessary to talk about blank lines... because the following text
is equivalent to only
one line of text
(or one paragraph):

.. code-block:: rst

    because the following text
    is equivalent to only
    one line of text
    (or one paragraph)

That is, a line break is reduced to just one space within reST, so to create a new paragraph we require an empty line between the two intended paragraphs (or, what is the same, two line breaks):

.. code-block:: rst

    This is a paragraph.

    And this is another paragraph, thanks to the empty line between both lines.

This brings us to the question: what happens if there are two blank lines? Or three? Or fifty? The result is the same: a paragraph change, nothing more.

What about the white space between each word? These collapse to just one. That is, the following:

.. code-block:: rst

    This           sentence    with         lots   of   spaces...

Is displayed as:

.. code-block:: rst

    This sentence with lots of spaces...

To sum up, keep three things in mind while writing in reST:

1. A paragraph change requires at least an empty line between both paragraphs.
2. Two or more empty lines have the same effect: a paragraph change.
3. Any number of tabs or spaces is reduced to one space.



What if you need more empty lines?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you need more whitespace between paragraphs, you can use a vertical bar as the only content of a given line. For example,

|
|

this longer space was achived with:

.. code-block:: rst

    For example,

    |
    |

    this longer space was achived with:



Quotes and indentation
----------------------


We can create blockquotes by indenting text. If I wanted to quote Martin Luther King, I just need to indent the line with at least one space:

    The tension is at bottom between justice and injustice, between the forces of light and the forces of darkness.

The quote above follows the following format:

.. code-block:: rst

    Paragraph

        Blockquote (notice indentation)

    Paragraph

In short, a paragraph has no space at the beginning, while a quote is indented with at least one space. "At least one" means that we can achieve the same with two spaces, or four, or ten, or tabs.


If we want to add an author to the quote, we can keep writing on another line, as long as we keep the same indentation as the other lines in the quote. For instance, the following:

.. _MLK quote:

    The tension is at bottom between justice and injustice, between the forces of light and the forces of darkness.

    Martin Luther King

was produced by the code in reStructuredText:

.. code-block:: rst

    The tension is at bottom between justice and injustice, between the forces of light and the forces of darkness.

    Martin Luther King

What if we want a quote within a quote? We create a new level of indentation (defined by any other number of spaces than the current one and larger than zero):

    The tension is at bottom between justice and injustice, between the forces of light and the forces of darkness.

        Martin Luther King

which was produced by code:

.. code-block:: rst

    The tension is at bottom between justice and injustice, between the forces of light and the forces of darkness.

        Martin Luther King

The example above can be summarized with the following pattern/example:

.. code-block:: rst

    Paragraph before the quote.

        First quote

            Second quote, by different indentation

        Back to quote one, by same indentation as "First quote"

    Paragraph after the quotes

that visually yields:

Paragraph before the quote.

    First quote

        Second quote, by different indentation

    Back to quote one, by same indentation as "First quote"

Paragraph after the quotes

|
|

With this example, two features of reST are evident:

1. Indentation matters.
2. But indentation can be any number of spaces larger than zero.

We need to address the aparent contradiction: reST does not care how many spaces are used for indentation, unless we are talking about creating different levels (defined as nesting).

When would we be creating different levels? When we use different number of indentation within a block that has not returned to a paragraph. The following example would have only one level, two times:

.. code-block:: rst

    First paragraph

        First level, with four spaces of indentation

    Second paragraph

            Still first level, but with eigth spaces (independent of the four-spaces level)

On the other hand, if both quoted sentences were not separated by a paragraph, they would be two levels (the first with four spaces and the second with eight):

.. code-block:: rst

    First paragraph

        First level, with four spaces of indentation

            Still first level, but with eigth spaces (independent of the four-spaces level)

    Second paragraph

If this is too much, don't worry. Soon it will become second nature while writing on reST.



Basic Formatting
----------------



Basic formatting covers three things: emphasis, boldface, and fixed-width font. In the cases mentioned, the opening symbol is used also at the end, as shown in the following table:

================ ======= ============================
Style            Symbol  Example
---------------- ------- ----------------------------
Emphasis         \*      *\*Text with emphasis\**
Boldface         \*\*    **\*\*Text in boldface\*\***
Fixed-width font \`\`    ````Fixed-width font````
================ ======= ============================

You must be aware of a caveat: you cannot mix these. That is, if you want emphasis with boldface, you are out of luck. That is, ***using three stars*** to enclose the target text won't work as you expect (the visual result is two starts used for boldface plus one printed star, which was not the expected result).

If you try to mix ``**fixed-width font with boldface**``, or **``boldface with fixed-width font``** will only yield the text with the outer formatting applied, printing the inner symbols.



Headers (Titles)
----------------


A header is a line of text that is followed by a line of identical symbols covering thxe length of the title. For example, the title of this chapter was written with the code:

.. code-block:: rst

    Basic Syntax
    ============

However, we could have used dashes instead:

.. code-block:: rst

    Basic Syntax
    ------------

Then, what symbols can be used under text to make a title? The oficial documentation says that "any ASCII non-alphanumeric 7-bits character". Or, the following list as reference: ``= - ` : ' " ~ ^ _ * + # < >``.

Based on this information, we could have written the title of the chapter as:

.. code-block:: rst

    Basic Syntax
    >>>>>>>>>>>>

While all those symbols can be used, a standard was put in place by Sphinx (but can also be followed when using reST alone):

- ``=``, for sections.
- ``-``, for subsections.
- ``^``, for subsubsections.
- ``"``, for paragraphs.

Another way to mark a title is using the same symbol in the line prior to the title, like:

.. code-block:: rst

    ============
    Basic Syntax
    ============

According to Sphinx, this can mark higher-level sections, like chapters or parts in a book, as follows:

- ``=``, above and below the title, for parts.
- ``*``, above and below the title, for chapters.

While those rules may be used for books or documents that need more title levels, most of the time you won't be using those (more typing, ugh).

Suffice to say that there are several ways to markup a title, and that the significance depends on the order of appearance.

This means that the symbols are used as first-come, first serve. For example:

.. code-block:: rst

    This is the title
    =================

    This is the subtitle
    --------------------

Is equivalent to:

.. code-block:: rst

    This is the title
    -----------------

    This is the subtitle
    ====================

While you can mix-and-match title symbols per file, it is better if you use a consistent standard across your files. For instance:

* ``=`` for titles
* ``-`` for subtitles
* ``^`` for subsubtitles.

If you need more levels, you have more symbols or the line-above-and-below syntax at your disposal.



What if the ruler ends up being shorter than the title?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If by any chance you end up with a ruler that is shorter that the length of the title, you will get a warning:

.. code-block:: none

    WARNING: Title underline too short.

    What if the ruler ends up being shorter than the title?
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [docutils]

And that's it. The title will be created as it should. However, aim for zero warnings on your documents, as those might confuse you when you face errors. Also, its a good rule to abide, acording to the `broken windows theory`_.



Comments
--------



To write comments within the document, start a new line with two colons and a space. What you write after that, will not show up in the output. For example:

.. This line is a comment and will not be shown.

.. code-block:: rst

    .. This line is a comment and will not be shown.

To write a comment with multiple lines, keep writing using at least one space for indentation. The standard is to use three spaces, so all lines in the comment are aligned:

.. This line is a comment.
   This line is, too.

   Everything will be, until there is a line with no indentation.

.. code-block:: rst

    .. This line is a comment.
       This line is, too.

       Everything will be, until there is a line with no indentation.

As shown in the example, the comment does not end with an empty line. The comment finishes until you have no more indentation (that is, when you create a new paragraph).



Lists
-----



There are three type of lists in reStructuredText:

* Unordered lists
* Ordered lists
* Definition lists

We'll see the unordered lists first, as we'll use them as example for nested lists and showing how to deal with whitespace.


Unordered lists
^^^^^^^^^^^^^^^



Unordered lists, or bulleted lists, can be created using the symbols star (``*``), plus (``+``), or dash (``-``), like:

- First element.
- Second element.
- Third element.

The code for this list was:

.. code-block:: rst

    - First element.
    - Second element.
    - Third element.

But we could have used a plus sign instead of a dash, like:

.. code-block:: rst

    + First element.
    + Second element.
    + Third element.

That is, it doesn't matter which symbol you use for unordered lists, the result will be the same bullet style. However, do not use more than one symbol per list, or you will face the next warning:

.. code-block:: none

    WARNING: Bullet list ends without a blank line; unexpected unindent.

Why? The reST processor got confused. It expects unordered lists to only use one symbol. If it finds two, it will assume one of the following is true:

1. The second symbol belongs to a different list. If this is the case, both lists should be separated by an empty line (but there isn't one in this case).
2. You are trying to nest lists, so the second item is a part of a daughter list. But for that, a change in indentation is required (which also is not the case).

However, the processor will still generate the proper list (with just one bullet symbol) after prompting you to solve the warning.



Nested lists
^^^^^^^^^^^^



If you want to create a list within a list, known as nested lists, you'll need to follow two reST rules, plus a LaTeX one:

#. Indentation on lists is not arbitrary: indentation for the item symbol of the nested list should match the first text character of the element of the parent list.
#. Each nested list should have an empty line that separates it from its parent list.
#. If you plan to use Sphinx/LaTeX to export to PDF, it only support four levels of nesting.

Let's address what each rule means, one by one.

For the first rule, let's get clear on what the words mean, with a sample text:

.. code-block:: rst

    First character is the symbol for an unordered list.
    │
    │Second character is a space (needed for lists to work).
    ││
    ││Third character is the starting text of the parent list.
    ↓↓↓
    * Parent list

      * Daughter list
    ↑ ↑
    │ Symbol of daughter list must match the position of the starting text of parent list.
    │
    Indentation is two spaces, because we must match parent list starting text.


From the text example we see that, for an unordered list, the first nested list should have an indentation of two spaces, because the parent item uses the ``*`` as item indicator, and it must be followed by at least one space.

Why the emphasis on the spacing? Because more than that, and the result will be a blockquote instead:

+ First level of list.

      - What is supposed to be the second level.

The code in reStructuredText was:

.. code-block:: rst

    + First level of list.

          - What is supposed to be the second level.

Depending on the theme, the blockquote may not be evident. To clarify this poing, I include the HTML generated code:

.. code-block:: html

    <ul>
        <li><p>Primer nivel</p>
            <blockquote>
                <div>
                    <ul class="simple">
                        <li><p>What is supposed to be the second level.</p></li>
                    </ul>
                </div>
            </blockquote>
        </li>
    </ul>

In order to avoid this unintended blockquote, the indentation should be exactly two spaces (aligning the "-" with the "F"):

.. code-block:: rst

    + First level of list.

      - What is supposed to be the second level.

This yields the expected result:

+ First level of list.

  - What is supposed to be the second level.

With cleaner HTML:

.. code-block:: html

    <ul class="simple">
        <li><p>First level of list.</p>
            <ul>
                <li><p>What is supposed to be the second level.</p></li>
            </ul>
        </li>
    </ul>

With the first rule explained, let's go to the second one: an empty line separating both lists.

Again, let's go directly to the sample:

+ First level of list.
  - What is supposed to be the second level.

The "lists" above come from the code:

.. code-block:: rst

   + First level of list.
     - What is supposed to be the second level.

The sublist doesn't get created: instead, it follows the "a single end of line is collapsed to a single space" rule.

Last, the rule about the nesting limit: LaTeX does not support more than four nesting levels... and you probably shouldn't make a deeply nested list anyway. But if you do, you may face the following error:

.. code-block:: none

    LaTeX Error: Too deeply nested.

    See the LaTeX manual or LaTeX Companion for explanation.
    Type  H <return>  for immediate help.

    l.114 \begin{itemize}


Again, this is not a problem you will find on the `online editor <https://rst-editor.ramoscarlos.com/>`_, where HTML can be arbitrarily nested.



What about the space after the list symbol?
"""""""""""""""""""""""""""""""""""""""""""


I forgot about the space after the symbol. Is it needed? The practical answer is:

+First element
+Second element

The code for the above attempt of list is:

.. code-block:: rst

   +First element
   +Second element

The answer is: the space is needed, otherwise the is no list. Another potential issue is that if we use the star symbol, reST will try to transform that to emphasis, and will yield the following warning:

.. code-block:: none

    WARNING: Inline emphasis start-string without end-string.

With that solved, what if we use more than one space to separate the bullet from the text? Then the code:

.. code-block:: rst

    + First element
    +      Second element

yields:

+ First element
+      Second element

The list is generated, even as both items have different spacing. What matters is that the list symbols are aligned, even whilst their content is not.



Ordered Lists
^^^^^^^^^^^^^


The ordered lists can be created with several characters, as unordered lists, but in this case the chosen character will determine the count style.

The first style that can be used is with arabic numbers:

1. Element.
2. Element.

For which code is:

.. code-block:: rst

    1. Element.
    2. Element.

That is, for ordered lists we need at least two characters as item indicator:

.. code-block:: rst

    Count style (arabic numbers, in this example)
    │
    |A dot, required to make an ordered list work
    ││
    ││Space, to separate indicator and text
    │││
    │││Start of content of the list item
    ↓↓↓↓
    1. Element.

If you miss the dot after the number, you will receive not get a list:

1 Element.
2 Element.

And now that we have seen the general form, we can add letters to the mix:

a. Element.
b. Element.

And that list was generated with the code below (notice the dot still after the letter):

.. code-block:: rst

    a. Element.
    b. Element.

Another option is uppercase letters:

A. Element.
B. Element.

Pretty sure you know the code at this point:

.. code-block:: rst

    A. Element.
    B. Element.

We also have roman numerals, both in upper and lower case, as:

I. Roman numeral one.
II. Roman numeral two.

i. Roman numeral one.
ii. Roman numeral two.

To err on the side of redundancy, the code is:

.. code-block:: rst

    I. Roman numeral one.
    II. Roman numeral two.

    i. Roman numeral one.
    ii. Roman numeral two.



Parenthesis
"""""""""""



Besides the five number styles described above (arabic, letters in lower and uppercase, and roman numerals in lower and uppercase), we can substitute the dot with parenthesis to indicate an ordered list, as:

.. code-block:: rst

    1. Hello.
    2. Good bye.

    1) Hello.
    2) Good bye.

    (1) Hello.
    (2) Good bye.

On HTML, the result is the same:

1. Hello.
2. Good bye.

1) Hello.
2) Good bye.

(1) Hello.
(2) Good bye.



Using the # symbol
""""""""""""""""""



We do not need to number the items. Instead of numbers (or any chosen sequence), the ``#`` (pound or hash) symbol can be used:

.. code-block:: rst

    a) First
    b) Second

    a) First
    #) Second

Both lists will display as:

a) First
#) Second

The first element will determine the style used. If you want arabic numbers, you can use the pound on item one:

.. code-block:: rst

    #) First
    #) Second

That will yield:

#) First
#) Second



Starting at another number
""""""""""""""""""""""""""



If you need to start the ordered list in other number (that is, not "one"), you can:

56. Element.
#. Element.
#. Element.

The code for the list was:

.. code-block:: rst

    56. Element.
    #. Element.
    #. Element.

Notice how only the first number was established, and reStructuredText took it from there for the following ones with the ``#``. This also works when working with letters,

e. First
#. Second
#. Third

where the list code is:

.. code-block:: rst

    e. First
    #. Second
    #. Third

.. note::

    Beware of the "i" and the "v" as starting numbers, as both characters can be either  a letter or a roman numeral. If you wanted the "i" as a letter, or the "v" as a roman numeral, that is not what you would get:

    v. This is roman 5.
    #. And this is roman 6.

    i. This is letter "i".
    #. This is letter "j".

    For which code was:

    .. code-block:: rst

        v. This is roman 5.
        #. And this is roman 6.

        i. This is letter "i".
        #. This is letter "j".



Nested Ordered Lists
""""""""""""""""""""



The ordered list can be nested, as unordered list. The only difference is that daughter lists minimum indentation is three:

.. code-block:: rst

    Count style (arabic numbers, in this example)
    │
    |A dot, required to make an ordered list work
    ││
    ││Space, to separate indicator and text
    │││
    │││Start of content of the list item
    ↓↓↓↓
    1. Parent list

       a. Daughter list
    ↑  ↑
    │  Symbol of daughter list must match the position of the starting text of parent list.
    │
    Indentation is three spaces, to accomodate for the dot required for ordered lists.

In case the parentheses are used, the minimum indentation would be four.

As the rules are the same, we'll jump straight to the example:

1. Arabic parent list

   i. Roman daughter list
   #. Roman next item

      * Unordered list
      * This is third level now

   #. This is roman 3.

      a) This ordered list makes no sense
      #) Prior third level was unordered
      #) As long as lists at the same level are separate entities
      #) This is not illegal (just confusing for the reader)

   #. Correctly numbered as "iv"

#. Let's close with arabic 2.


The code for the list above is:

.. code-block:: rst

    1. Arabic parent list

       i. Roman daughter list
       #. Roman next item

          * Unordered list
          * This is third level now

       #. This is roman 3.

          a) This ordered list makes no sense
          #) Prior third level was unordered
          #) As long as lists at the same level are separate entities
          #) This is not illegal (just confusing for the reader)

       #. Correctly numbered as "iv"

    #. Let's close with arabic 2.



Definition Lists
^^^^^^^^^^^^^^^^

A definition list is a type of list that has terms and definitions. The format of a definition list is:

.. code-block:: rst

   Term without indentation
   ↓
   term
     definition
     ↑
     The definition is right below it, no empty line
     Indented any number of spaces

The term and definitions as follows:

term
  The term has no indentation.

definition
  The definition is below the term, indented.

The code is:

.. code-block:: rst

    term
      The term has no indentation.

    definition
      The definition is below the term, indented.


.. _preformatting:

Preformatting (code samples)
----------------------------

Preformatting means that the text does not get converted by the reST processor, and that the blank space is kept intact. It is marked with two colons (``::``) followed by an empty line, like:

::

    ::

        This is preformatted text, as it's under two colons.
        No *markup* symbols are _transformed_.

If there is no empty line between the two colons and the preformatted text, it won't display as expected:

::
    This should be preformatted text...
    But isn't, because an empty line is needed

If you put the two colons at the end of a sentence, one colon will be appended at the end of the sentence, and the text that follows will be preformatted::

    This block did not start with "::" by itself on a line.

    But the last paragraph finished with "::".

        So this block keeps the space intact.



External Links
--------------



An external link is a link which address/URL leads to outside your document (most likely a website). Such links can be created in two ways: directly or indirectly.



Direct Links
^^^^^^^^^^^^


The direct link is embedded in line with text. A link starts with a grave accent (`````), followed by the text to display, then the destination between the less than (``<``) and greater than (``>``) symbols, finishing with another grave accent and an underscore (``_``). For example:

.. code-block:: rst

    `display text <target destination>`_

Based on that syntax, if we want to visit `Python's website <https://www.python.org/>`_ we can use the following code:

.. code-block:: rst

    `Python's website <https://www.python.org/>`_



Indirect Link
^^^^^^^^^^^^^

Direct links can become difficult to read when the display text or the destination are long (or worse, both!). In such cases, it might be easier to read if we opt to separate the display text from the target. This can be done using the indirect link syntax, which divides a link in two parts:

#. The display text
#. The display text plus the target URL.

That is, we can write Python_ (written as ``Python_``) and have that be the link. If we compile like that, a warning is issued:

.. code-block:: none

    WARNING: Unknown target name: "Python".

That is, the definition of the target hasn't been given yet. The definition of a link can be done in any place of the document, with the recommended spot being at the bottom of the document. If we add this line anywhere in the document, then the link works:

.. code-block:: rst

    .. _Python: https://www.python.org/

To create the definition, the following syntax was used (dot, dot, space, underscore, display text, colon, space, target URL):

.. code-block:: rst

    .. _Display text: target-URL

As seen in the example above, we can use several words as the `Display Text`_ (this link will lead to Python site, too). When at least two words are used, then the words must be surrounded by grave accents (```Display Text`_``).

Notice how the reference needs grave accents, but those are not used in the definition part.



Internal Links
--------------



Internal links are references that take us to a place within our own document. They are like the content links in a Wikipedia entry.

They follow the same syntax as an external indirect link for the references, with one tiny change to the definition part: it omits the target URL, as the target will become whatever content is right behind it.

If we wanted to go back on this chapter to the `MLK quote`_ (```MLK quote`_``), we just need to add this code right above the desired content:

.. code-block:: rst

    .. _MLK quote:

In general, you need to add the ``.. _link text:`` text in an empty line above the content you plan to reference, then use the ```link text`_`` anywhere you want to reference that content.



Implicit Links
^^^^^^^^^^^^^^



Implicit links are internal links automatically created with section headers (titles). That is, you can point directly to a section, like `Basic Syntax`_ (```Basic Syntax`_``) and you will be taken there.

You can jump to the `ordered lists`_ or `comments`_, too: reStructuredText makes *all* it's titles a usable reference.

The only disadvange to implicit links is that they must match the title exactly, albeit case is ignored.



Tables
------



There are two ways to make tables in reST: the bad way and the worse way. To tell you the truth, there is no joy in plain text tables. You have one item bigger than expected, and suddenly you need to go back and align everything back again. A disaster.

Of course, this is not a problem to reST alone, all markup languages are just not writer-friendly when it comes to building tables. Is at this darkest hour when one shall bow to the superiority of a graphical interface and head to `tablesgenerator.com`_. Thanks to this website, we can generate a beautiful text table, with less effort:

.. code-block:: rst

    +-------------------------+-------------+-------------+
    | Multicolumn             | Header4     | Header5     |
    +-----------+------+------+-------------+-------------+
    | Multirow  | R2C2 | R2C3 | R2C4        | R2C5        |
    |           +------+------+-------------+-------------+
    |           | R3C2 | R3C3 | R3C4        | R3C5        |
    +-----------+------+------+-------------+-------------+
    | R4C1      | R4C2 | R4C3 | R4C4        | R4C5        |
    +-----------+------+------+-------------+-------------+

In reST, the header is marked with a line of equal signs below (``=``) the first row, so that is the only change we need to do to make a plain text table a resTructuredText table:

.. code-block:: rst

    +-------------------------+-------------+-------------+
    | Multicolumn             | Header4     | Header5     |
    +===========+======+======+=============+=============+
    | Multirow  | R2C2 | R2C3 | R2C4        | R2C5        |
    |           +------+------+-------------+-------------+
    |           | R3C2 | R3C3 | R3C4        | R3C5        |
    +-----------+------+------+-------------+-------------+
    | R4C1      | R4C2 | R4C3 | R4C4        | R4C5        |
    +-----------+------+------+-------------+-------------+


All that mix of ``-`` to separate rows, ``|`` to separate columns, ``=`` to markup the header, and ``+`` for the intersections, is now the reST table:

+-------------------------+-------------+-------------+
| Multicolumn             | Header4     | Header5     |
+===========+======+======+=============+=============+
| Multirow  | R2C2 | R2C3 | R2C4        | R2C5        |
|           +------+------+-------------+-------------+
|           | R3C2 | R3C3 | R3C4        | R3C5        |
+-----------+------+------+-------------+-------------+
| R4C1      | R4C2 | R4C3 | R4C4        | R4C5        |
+-----------+------+------+-------------+-------------+

If this is too complex for you, there is a silver lining in all of this: what I showed you first was the "worst" way. Let's see the "bad" way.

The "bad" way of doing tables is simpler than what we saw above. Still a pain to write, but simpler. The drawback? No multirow is allowed, so this method will be out of the table when multirow capabilities are needed.

Having said that, here is tha example:

.. code-block:: rst

    =============== =================
    Header1         Header2
    =============== =================
    Row 2, Column 1 Row 2, Column 2
    Row 3, Column 1 Row 3, Column 2
    =============== =================

This kind of table required three things:

#. Columns have a fixed-width (all elements in a column have the same length, and padded with spaces if not).
#. The first and last lines indicate the columns with equal signs (``=``).
#. The line below the header (first row) also should be filled with ``=`` signs.
#. There should be at least one space between columns, but could be more.

Here is the displayed table for the code above:

=============== =================
Header1         Header2
=============== =================
Row 2, Column 1 Row 2, Column 2
Row 3, Column 1 Row 3, Column 2
=============== =================

Each group of equal signs defines the max width of the column. If the content in a column is larger than the equal signs above or below it, a warning will be issued:

.. code-block:: rst

    WARNING: Malformed table.
    Text in column margin in table line 2.

    =============== =================
    A very long Header1 Header2
    =============== =================

In this case, the document will be generated without the table. That is, as simple as this format is, you can mess all the table for one tiny space.

Again, I recommend using the table generator online at `tablesgenerator.com`_. Copy, paste, and change the header line. That's it.



Summary
-------


In this chapter we saw the reStructuredText syntax for our most common text needs. We saw how paragraphs were defined, the importance of empty lines and indentation, and the use of **\*\*boldface\*\*** and *\*italics\**, and how to include titles, lists, comments, and even links and tables.

However, we can do more stuff with reST using directives. We'll see those in the next chapter.



.. #######################################################################
.. ### External links ####################################################
.. #######################################################################

.. _broken windows theory: https://en.wikipedia.org/wiki/Broken_windows_theory
.. _Python: https://www.python.org/
.. _Display Text: https://www.python.org/
.. _tablesgenerator.com: https://www.tablesgenerator.com/text_tables
