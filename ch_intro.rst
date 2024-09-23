Introduction
============


This book exists for a sole reason: there is not much material about reStructuredText. That's a shame, because it is an incredible tool to write training material on.

I came accross this tool thanks to my work, where I had to find a way to ease the onboarding process for the new hires. The existing documentation comprehended heavy Microsoft Word files that were mostly unread, and a wiki site that had some complex SQL queries we copied and pasted whenever they were needed.

New security policies came into effect, and the wiki was flagged as a risk. With that, our team was given some reasonable time to take all our belongings and abandon the sinking documentation ship. The task to train people was still mine, but I had lost most of the onboarding library with the closure.

While Microsoft Word was the suggested answer when we asked for a replacement for our wiki, that processor is a poor tool because it violates the *Don't Repeat Yourself* (DRY) principle. That is, each time we performed an update in our SQL scripts, we would have to go and review the Word document also.

Unhappy, I was on the market for another technology. The popular choice among programmers and technical writers was Markdown. However, it shared the same weak spot with Word: the SQL queries would have to be copied into each Markdown entry, as vanilla Markdown had no way to include files. While there are flavors of Markdown capable of including files, that was yet another layer of abstraction I would need to train people on.

Why would I care about that? Well, I was not only responsible of writing, publishing, and distributing the documentation. On top of that, I would be responsible of training my peers at work on how to document their stuff (after all, I was just a leader on my area, not the technical writer of all the processes).

Therefore, I needed a documentation technology that:

* allowed multiple authors
* allowed source code file inclusions
* did not use a database as repository (due to security concerns)
* yielded a PDF

I kept looking, until I found *reStructuredText* (from here on, *reST*, *rst* and *reStructuredText* are all interchangeable): a markup syntax designed by programmers to generate documentation.

This book is the result of my experience with the language. I hope you can find in this book the answers you need to start using *reST* as your documentation writing and generation tool.


How to read this book?
----------------------


This book is designed to be a reference for the common elements of reStructuredText. If you are new to *reST*, I recommend reading the entire book to get an idea of what you can do with it. If you are already familiar with the language, you can use this material as a reference to remember elements of the syntax.

.. note::

	This work shows the source code in *reST* and its output to screen (well, to the book). That is, the code generated in HTML or LaTeX will not be seen, since this work is aimed at people without prior knowledge of markup languages.


Contributing
------------


This book is open source and you can contribute with it if you are familiar with git. The repository is hosted on GitHub_, and you can check the guidelines for contributing at CONTRIBUTING_.


Found a problem?
----------------


In case you find a typo or an error in a code sample, you can `open an issue`_ on GitHub. I will work on solving these :D.



.. _GitHub: https://github.com/ramoscarlos/rst-guide
.. _CONTRIBUTING: https://github.com/ramoscarlos/rst-guide/blob/master/CONTRIBUTING.md
.. _open an issue: https://github.com/ramoscarlos/rst-guide/issues
