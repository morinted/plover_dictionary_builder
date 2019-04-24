=========================
Plover Dictionary Builder
=========================
Add new vocabulary to your dictionaries faster than ever before
----------------------------------------------------------------

.. image:: https://i.imgur.com/f48fKwv.png
   :width: 400 px

Release Notes
-------------

v0.1.0
======

- Add option to have a translation per line.
- Add option to transform text to upper or lowercase.

How to Use
----------

Part 1: Selecting Text
======================

#. Get a word list or article to scan for vocabulary.
#. Paste your text into the dictionary builder.
#. For building up with word lists or phrases, you can select
   "Treat each line as one translation".
#. Select whether you'd like to see words that are already defined
   in your dictionary. If you only want to see new words, leave this unchecked.
#. Apply a text transformation if you'd like to avoid being case-sensitive or
   must work in all caps.
#. Click "Start Building".

Part 2: Building
================

See the various parts of the builder:

.. image:: https://i.imgur.com/egW4Ps3.png
   :width: 400 px

1. Progress indicator
2. Entry definer:

   - Dictionary: the dictionary that the next stroke will go into on "Add".
   - Strokes: Your steno machine will write with raw steno into the strokes box. This is how you will define your desired strokes.
   - Translation: auto-filled as you go through words, but can be edited if needed.

3. What's in your dictionary:

   - The first box contains what your current steno maps to in your dictionaries.
   - The second box shows you how it's currently possible to write the target word.
   - Both these boxes update as you create new strokes.

4. The word order. You can tackle words from your text in several orders, which should help with different kinds of texts you might be working on. The options are:

   - Frequency: most frequently used words in the text appear first.
   - Order of Appearance: unique words in the order that they appear in the text.
   - Alphabetical: unique words sorted alphabetically.

5. The word list. The selected word is the current one being defined. You can clicked on any word to jump to it.

6. The controls:

   - **Back to Input**: stop building and go back to the text-entry

     - Keyboard shortcut: **Escape, close button, or Ctrl W**

   - **Previous**: change "Translation" to previous word

     - Keyboard shortcut: **Up**

   - **Next**: change "Translation" to next word

     - Keyboard shortcut: **Down**

   - **Undo**: remove the last definition you made

     - Keyboard shortcut: **Ctrl Z** (you might need to make sure you aren't in a text box for this shortcut to activate)

   - **Add and Next**: add the strokes and translation to the selected dictionary then go to the next word

     - Keyboard shortcut: **Ctrl S**

   - **Add**: add the strokes and translation to the selected dictionary and keep the current word for another definition

     - Keyboard shortcut: **Return/Enter**

All changes you make in the dictionary builder are saved automatically as you go.

License
=======

This plugin is licensed under GPLv2, or any later version.
