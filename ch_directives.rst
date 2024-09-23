Directives
==========


As defined by the `reStructuredText documentation <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#directives>`_, the directives are an extension mechanism. This means that developers can add functionality as they see fit. And, if you want to learn and do something not currently possible, you can do so.

However, for most of us not planning to extend current capabilities, directives are complex instructions that abide to the following syntax:

.. code-block:: none

    .. directive-name:: arguments
       :option1:
       :option2:

       content

There is a lot to unpack in the code shown above. First, let's talk about the directive marker, which includes three things:

#. The starting two periods and a space (starting almost like a comment).
#. The ``directive-name``, which will identify what the directive will be.
#. The two colons, which wraps the directive marker.

The directive marker is required (all three parts already mentioned). However, there are other three parts of a directive we haven't mentioned: arguments, options, and content.

The distinction between arguments, options and content are up to the directive, so an explanation without some context or knowledge of a few directives would be a headache.

Let's jump straight into our first directive: ``image``.



Image
-----


The ``image`` directive is used with a required argument: the directory, path, or URL of the image. For instance, here I include my logo, hosted on my personal domain:

.. image:: http://ramoscarlos.com/logo.png

All I had to type was:

.. code-block:: rst

    .. image:: http://ramoscarlos.com/logo.png

However, depending on your browser or e-reader, the width of the image might be too much. As reStructuredText did no processing to the image (like scaling or setting maximum width), the limits are imposed by the device.

As this may not be what is required for the image, we have *options* to modify *how* the image is shown. Some of the options for the ``image`` directive are:

:height: is the height of the image, use to reserve the vertical space. When used along with ``scale``, both parameters are applied (i.e. if height is 100px, and scale is 40%, then final height will be 40px).
:width: is the width of the image, which can be given as an absolute value or relative percentage. As ``height``, this can also be combined with ``scale``.
:scale: is the uniform scaling factor of the image. IT's value is expressed in percentage, and its default value is 100% (which means no scaling).
:align: defines where the image will be placed relative to its container. Values can be ``top``, ``middle``, ``bottom`` for vertical alignment, and ``left``, ``center``, o ``right`` for horizontal alignment.
:alt: is an alternative text that is displayed in case the image cannot be loaded.
:target: transforms the image into a link, that points to the URL specified in this field.

Let's first test the ``:alt:`` option with a non-existant image:

.. image:: http://this-image.shall/not-exits.gif
   :alt: This text should be displayed instead

.. raw:: latex

    \begin{sphinxVerbatim}
    This text should be displayed instead
    \end{sphinxVerbatim}

And that magic was done with the code:

.. code-block:: rst

    .. image:: http://this-image.shall/not-exits.gif
        :alt: This text should be displayed instead

To solve the size issue, we can use the option ``width``, with a percentage value of 60%. As align is not used, image will be left-aligned:

.. code-block:: rst

    .. image:: http://ramoscarlos.com/logo.png
        :width: 60%
        :alt: ramoscarlos.com logo

.. image:: http://ramoscarlos.com/logo.png
    :width: 60%
    :alt: ramoscarlos.com logo



Local images
^^^^^^^^^^^^



The ``image`` directive is not limited to online resources. However, that is something that cannot be tested on the online editor. In case you want to try this out in your machine, the best way to use reStructuredText locally is to install Python3 and Sphinx.

When working locally, you can use the relative path of the image in the directive:

.. code-block:: rst

    .. image:: img/image-name.png

Sphinx is out of scope on this book, but feel free to try it.



Figures
-------


A figure is an image with a legend. Its syntax is similar to the ``image`` directive, even the options are the same. The difference? ``figure`` uses the content of the directive as the legend to the image. The syntax is:

.. code-block:: rst

    .. figure:: img/image-name.png

        Legend.

You can take one of the examples above and add the legend on the directive content:

.. code-block:: rst

    .. figure:: http://ramoscarlos.com/logo.png
        :width: 60%
        :alt: ramoscarlos.com logo

        ramoscarlos.com logo (with legend)

That is all that we need to have an image with a legend below:

.. figure:: http://ramoscarlos.com/logo.png
    :width: 60%
    :alt: ramoscarlos.com logo

    ramoscarlos.com logo (with legend)



Code (Embedded)
---------------

As far as code goes, we are not limited to :ref:`preformatting <preformatting>`. We can include source code with syntax highlighting with the ``code`` directive, that receives the language as an argument. The syntax highlighting is provided by the Pygments_ library, which means that all the languages supported by the library are available for your documentation purposes.

As an example, here is a fragment of C code:

.. code:: c

    int main() {
        return 0;
    }

This code shows the right coloring thanks to the language argument:

.. code-block:: rst

    .. code:: c

        int main() {
            return 0;
        }

You can highlight reStructuredText:

.. code:: rst

    This has *emphasis*, while this has **bold face**.

And the code for the directive example is:

.. code-block:: rst

    .. code:: rst

        This has *emphasis*, while this has **bold face**.

.. note::

    The online editor does not load the syntax highlighting styles, as that means more processing. Yes, it's frustrating. However, doesn't that make you want to try Shpinx even more?



Opción ``number-lines``
^^^^^^^^^^^^^^^^^^^^^^^


The ``code`` directive has an option called ``number-lines``, which allows us to add line numbers at the beginning of each line. For instance, we can add them to the C sample:

.. code-block:: rst

    .. code:: c
        :number-lines:

        int main() {
            return 0;
        }

Which will now display the code as:

.. code:: c
    :number-lines:

    int main() {
        return 0;
    }

If we want to imply this is a fragment, we can add the option argument after the option colon:

.. code-block:: rst

    .. code:: c
        :number-lines: 50

        int main() {
            return 0;
        }

Thus, the first printed line of code will be numbered as line 50:

.. code:: c
    :number-lines: 50

    int main() {
        return 0;
    }

By the way: if you miss the space between the option and its argument (i.e. ``:number-lines:50``), you will get a warning and the code will not show up:

.. code-block:: none

    WARNING: Error in "code" directive:
    maximum 1 argument(s) allowed, 2 supplied.

    .. code:: c
            :number-lines:50

            int main() {
                    return 0;
            }



Code (external file)
--------------------

Rather than copying the source code into the reStructuredText entry, you can rather include its full contents by reference, with the ``include`` directive. As with the local image example, this is something that you cannot test in the online editor.

As the ``image`` directive, ``include`` uses its first argument to reference the source code file the directive will include in the documentation. For the purposes of this example, the sourcecode files will be kept at the subdirectory ``src``.

The demo here points to the `Python's official documentation <https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example>`_, stored locally as ``demo.py``. To include the file we type:

.. code-block:: rst

    .. include:: src/demo.py

Which outputs the code into the book:

.. include:: src/demo.py

Well, what lies above is a poor attempt at including the code, at best. There is no syntax highlighting, and some end of line characters were striped, too. This was because the interpreter believed that the included source file was reStructuredText (it does that by default).

That is, the ``include`` directive is to make a full document with reStructuredText, like including a chapter rst file within a book rst file. However, the common usage of this directive is to add source code. To make it act as such, we need to use the ``code`` option.



``code`` option
^^^^^^^^^^^^^^^


The errors in trying to parse code as reStructuredText can go away using the ``code`` option, which receives as its argument the language the code is written in. In essence, its the same as the ``code`` directive argument (that it, it can take any Pygment-supported language). Let's try:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python

Now the code displays as Python code, and lines are crammed together:

.. include:: src/demo.py
    :code: python



``number-lines`` option
^^^^^^^^^^^^^^^^^^^^^^^

The ``number-lines`` works just as the option on the ``code`` directive... in theory:

.. include:: src/demo.py
    :code: python
    :number-lines:

As you can see, the syntax colors are gone. Lesson: use ``code`` if coloring needs to be accomplished along with line numbers.



``start-line``/``end-line`` options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


A fragment of code can also be included specifying a starting line numbers, up to an ending line number. For instance, to include only the ``do_global`` function (lines 9 to 11), the option ``start-line`` can be used with a value of 8 (as the count starts at 0). Therefore, ``end-line`` option will have an 11, as the last number does not get printed:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :start-line: 8
        :end-line: 11

Which shows the three target lines of code:

.. include:: src/demo.py
    :code: python
    :start-line: 8
    :end-line: 11



``start-after``/``end-after`` options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What if we want to print the ``do_global`` function not depending on the line numbers? For that, we would need to know a string we can use as a starting point. Such option is called ``start-after``, which receives a string to search for (which will not be printed).

As the function starts after the ``"nonlocal spam"`` line, that can be used as value for the option:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :start-after: "nonlocal spam"

This shows:

.. include:: src/demo.py
    :code: python
    :start-after: "nonlocal spam"

However, notice how the usage of this option yields code without syntax highlighting.

In case we want to use the end condition, we can try with ``spam = "test spam"`` as value for ``end-before``:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :start-after: "nonlocal spam"
        :end-before: spam = "test spam"

Which will yield the same code as having used the line numbers options:

.. include:: src/demo.py
    :code: python
    :start-after: "nonlocal spam"
    :end-before: spam = "test spam"



``tab-width`` option
--------------------

The ``tab-width`` options allows you to control how many spaces are show per tabulation character. By default, the value is set to eight. To change that to two, we can use:

.. code-block:: rst

    .. include:: src/demo.py
        :code: python
        :tab-width: 2

With the same file, notice the difference in spaces:

.. include:: src/demo.py
    :code: python
    :tab-width: 2

In case this option yields no different output, check the file. It may use spaces instead of tabs (as any decent human being should).



Inserting HTML or LaTeX with ``raw``
------------------------------------



If you feel the urge to use HTML in your reST document, is not that simple. For instance, let's add an horizontal ruler:

<hr>

Yeah... that did not work. To insert HTML we need to use the ``raw`` directive, with the language to be used as its argument. In this example, the language is ``html``: este caso es ``html``:

.. code-block:: rst

    .. raw:: html

        <hr>

That displays the ruler:

.. raw:: html

    <hr>

However, there is no such rulers for the PDF readers. That is because the PDF is compiled with LaTeX, not with HTML (a reason against using raw HTML). If we want to add an horizontal rule on the PDF we can use the ``\rule`` command on a LaTeX environment:

.. code-block:: rst

    .. raw:: latex

        \noindent{\rule{\linewidth}{0.4pt}}

This will give us the horizontal ruler on the PDF, but not on the HTML page:

.. raw:: latex

    \noindent{\rule{\linewidth}{0.4pt}}

We can include as much HTML or LaTeX we desire, but we need to provide two instructions if we intend that our documentation looks good on a webpage, a printed book, or an ereader. To guarantee the presence of all required elements, both ``raw`` directives can be included one after the other:

.. code-block:: rst

    .. raw:: html

        <hr>

    .. raw:: latex

        \noindent{\rule{\linewidth}{0.4pt}}

This way, the webpage and the PDF version have a ruler:

.. raw:: html

    <hr>

.. raw:: latex

    \noindent{\rule{\linewidth}{0.4pt}}



Admonitions
-----------



Admonitions are special messages. You can picture them as colored boxes: red for errors, yellow for warnings, blue for information.

The admonition is a set of directives. Yes, you have the generic ``admonition``, but you have several others at your disposal: ``attention``, ``caution``, ``danger``, ``error``, ``hint``, ``important``, ``note``, ``tip``, and ``warning``.

Depending on the HTML theme, each of the admonitions has a different style. The syntax is:, y se mandan llamar de la siguiente forma:

.. code-block:: rst

    .. admonition-type::

        Admonition content.

For example, to display a warning admonition, type:

.. code-block:: rst

    .. warning::

        Admonition content.

Now, each admonitions type, to compare style:

.. attention::

    Content for type ``attention``.

.. caution::

    Content for type ``caution``.

.. danger::

    Content for type ``danger``.

.. error::

    Content for type ``error``.

.. hint::

    Content for type ``hint``.

.. important::

    Content for type ``important``.

.. note::

    Content for type ``note``.

.. tip::

    Content for type ``tip``.

.. warning::

    Content for type ``warning``.

Each admonition type comes with a title, except the generic one. As it doesn't come with a default title, it is required as an argument:

.. code-block:: rst

    .. admonition:: Admonition title

        Content for type ``admonition``.

Lo que da como resultado:

.. admonition:: Admonition title

    Content for type ``admonition``.



Math
----


Yes! reStructuredText is  also used to write complex math equations... well, sort of. For this, it uses LaTeX. If you know LaTeX, all you need to know is that you can use it with the ``math`` directive, as:

.. code-block:: rst

    .. math::

        \frac{1}{2} + \frac{1}{4} + \ldots = \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n = 1

Which gets displayed as:

.. math::

    \frac{1}{2} + \frac{1}{4} + \ldots = \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n = 1

If you do not understand LaTeX, `I wrote a book about it`_ (on Spanish, though).



Extensibility
-------------


On the first chapters I talked about reST extensibility, but not much was said on the *how*. At the beginning of this chapter we saw that a directive is a name between the ``..`` and the ``::``. In theory, we can make a directive to display an attendance list:

.. code-block:: rst

    .. attendance-list::
        :class: Algebra

        John Smith
        Lara Croft

With some programming magic, that can print as a table with dates and everything needed. If you want to know more, you can read the `Creating reStructuredText Directives`_ documentation.

While Markdown added functionality via flavors and third-party modifications, reST was born with this extensibility in mind. There is even a way for your contributions to be added to the official repository, so people can install your extension easily.

At this point, we are done with the reStructuredText guide, and you are ready to learn about Sphinx.



Summary
-------


We learned about reStruturedText directives on this chapter, which are more powerful instructions, born out of the language extensibility mechanism.

We limited ourselves to look into the reST-defined directives, but you can go and see what else is out there that may help your documentation needs.



.. #######################################################################
.. ### External links ####################################################
.. #######################################################################

.. _Pygments: https://pygments.org/languages/
.. _I wrote a book about it: https://leanpub.com/tesis-en-latex/
.. _Creating reStructuredText Directives: https://docutils.sourceforge.io/docs/howto/rst-directives.html
.. _sphinx-contrib: https://github.com/sphinx-contrib/
