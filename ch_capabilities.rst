What can we do with reST?
=========================



We've already seen that reST is an efficient writing language and it's useful because it can be converted to other formats... but what are those formats? What are the real benefits of writing in reST and then translating?

In this chapter we'll look at the formats that reST can be converted to, in two main sections. First, what you can do from the online editor and, second, what you can do from Sphinx. The latter is mentioned briefly so that you know the scope of what reST can help you achieve.



With the online editor
----------------------



Compiling with the online editor allows two output formats:

+ HTML (web page)
+ PDF

This is enough for the scope of this book, as it will allow you to test the potential of reST and its syntax, and then decide whether you want to continue your journey with Sphinx.

It's also useful: you can export to PDF to easily share your notes with others.


With Sphinx
----------



If you decide to continue your journey with *reST*, the logical step is learning Sphinx. But, what will Sphinx allow you to do?



Websites
^^^^^^^^



You'll be able to create full-fledged, multi-page websites because Sphinx features a static HTML site generator. Yes, it's geared towards project documentation, but that doesn't stop you from creating a blog out of it (especially if you don't require comments on your site).



Documents
^^^^^^^^^



In addition to generating the site, you can convert to PDF (although you already suspected as much, as the online editor can do it). However, Sphinx conversion from reST to PDF is done via LaTeX. If you're familiar with that language, you can also customize the output format of your PDF.

Imagine: being able to create a website from your content and an entire book in PDF format. All with the same source code.

Of course, I'm not saying you'll make a document as spectacular as all the options in Microsoft Word, or other specialized PDF editing programs, but this book you are reading was created with Sphinx, all written in reStructuredText. Don't you think that's great?



eBooks
^^^^^^



Didn't we just mention PDF in the previous section? Yes, but that's not what I'm talking about. I'm talking about the EPUB electronic book format. After all, EPUB is a subset of HTML, so why wouldn't that be possible?

If you want to write a book independently, you can use Sphinx and reST to write once and export to both PDF and EPUB, plus you can have your book online in HTML. Three formats for the price of one. Why not?



Notes
^^^^^



The reST format is also quite useful for writing quick notes. You put a title, and start a bullet list quickly. That way you can start the list of what you need to buy at the supermarket, or the to-do list for the day.

Taking notes at work? You can create one file and separate each category with a subtitle, and that's it. Much better than having plain text notes.

The bad: for taking notes in reST there are not many online platforms nor apps for your smartphone. You can only do it in the online editor provided in this book or on your computer locally with a program like `Visual Studio Code`_ or `Sublime Text`_, using syntax highlighting for *\*.rst* files.



Documentation
^^^^^^^^^^^^^



Documentation is where reStructuredText, in conjunction with Sphinx, shines. Sites like `Read The Docs`_ and `Write The Docs`_ are powered by Sphinx.

If you have an open source project and want to publish documentation, you can link your GitHub repository to a `Read The Docs`_ project and *voilà*, documentation available!



Summary
-------



In this chapter we saw that reST can be used to make notes in an online editor, which converts reST code into visually pleasing HTML. In addition, this editor allows you to export the content to a PDF, a convenient way to take notes!

Furthermore, in conjunction with Sphinx, reST can create complete documentation websites, as well as complete books in PDF or EPUB format. What more could you ask of reStructuredText?



.. _Visual Studio Code: https://code.visualstudio.com
.. _Sublime Text: https://www.sublimetext.com/
.. _Read The Docs: https://readthedocs.org/
.. _Write The Docs: https://www.writethedocs.org/
