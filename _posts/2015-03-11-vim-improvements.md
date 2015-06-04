---
layout: post
title: Vim improvements
---
These are things I think Vim needs improving on. Maybe I'll fix them some day.

- Next section matching should be changed to matching the next line that is on the same alignment level. Would be useful to select environments in LaTeX

- Faster regex matching

- A latex IDE that is minimal (doesn't clutter your maps) but provides solid functionality for compiling, viewing, indentation and error parsing. I have a set up that nearly does this.

- There is a very subtle bug in <a href="http://www.vim.org/scripts/script.php?script_id=2325">this script</a> related to how it finds filenames. See <a href="https://gist.github.com/texasflood/b330df17f74c90e2b5da#file-latexerrorfilterbug-L44">this line</a> of the pdftex error output. The `(...` is interpreted as though the filename is `..` because the standard format for the filename is `(./fileName`. I would fix it but I'm not too familiar with gawk.

- (Actually maybe this is because I wasn't in insert mode...) The auto indent paste hack sometimes chops off the first few characters sometimes. This is the hack, put this in your `.vimrc`:

{% highlight vim %}
inoremap <special> <expr> <Esc>[200~ XTermPasteBegin()
function! XTermPasteBegin()
  set pastetoggle=<Esc>[201~
  set paste
  return ""
endfunction
let &t_SI .= "\<Esc>[?2004h"
let &t_EI .= "\<Esc>[?2004l"
{% endhighlight %}

And now you will never need to type `:set paste` when pasting a large body of code again. It's almost voodoo.

- Ability to use the repeat number feature for both inline operations and multiline operations. E.g. typing `2>>` indents two lines by one indent to the left. There should be an option like `-2>>` to indent one line twice.

- Undo diff (undojoin?)

- Case insensitivity for filename completion when using `:e filename`. Better filename tab completion, e.g. don't complete to buffers that are already open. Maybe even add an option to not autocomplete files with `.swp` or `.swo` files as they are probably open elsewhere

- Not requiring a space prepending a string which you want to filename complete (`^X^F`)

- I don't understand why I should have to put `nnoremap cw dwi` in my `.vimrc`

- The repeat operation applied to `J` in normal mode applies one less repeat than I expect

- Have a way of storing previous commands, so `.` can be modified so older commands can be called

- When opening giant files, the numbering pane on the left is set to the maximum size of the largest line no. This could be made be more efficient.

- Create a plugin that adds shortcuts for mathematical manipulations more easily. E.g. `Ctrl-A` adds to the next number (unless a minus sign precedes it). More shortcuts could be added to subtract and add regardless of a preceding minus sign. Also, float support would be good, but complex.

- Changing colorschemes is not smooth. E.g. make default `badwolf`, change to `koehler` and then change back to `badwolf`. Then visual mode retains the appearance of `koehler`.

- The rules that govern how the numbered registers work are inconsistent:

<table>
  <tr>
    <th>operation</th>
    <th><code>""</code> (default)</th>
    <th><code>"0</code> (yank)</th>
    <th><code>"1</code> (numbered)</th>
    <th><code>"a</code> (named)</th>
    <th><code>"-</code> (small&nbsp;delete)</th>
  </tr>

  <tr>
    <td><code>yw</code></td>
    <td>X</td>
    <td>X</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>

  <tr>
    <td><code>yy</code></td>
    <td>X</td>
    <td>X</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>

  <tr>
    <td><code>"ayw</code></td>
    <td>X</td>
    <td>-</td>
    <td>-</td>
    <td>X</td>
    <td>-</td>
  </tr>

  <tr>
    <td><code>"ayy</code></td>
    <td>X</td>
    <td>-</td>
    <td>-</td>
    <td>X</td>
    <td>-</td>
  </tr>

  <tr>
    <td><code>dw</code></td>
    <td>X</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>X</td>
  </tr>

  <tr>
    <td><code>dd</code></td>
    <td>X</td>
    <td>-</td>
    <td>X</td>
    <td>-</td>
    <td>-</td>
  </tr>

  <tr>
    <td><code>"adw</code></td>
    <td>X</td>
    <td>-</td>
    <td>X</td>
    <td>X</td>
    <td>-</td>
  </tr>

  <tr>
    <td><code>"add</code></td>
    <td>X</td>
    <td>-</td>
    <td>X</td>
    <td>X</td>
    <td>-</td>
  </tr>
</table>

Taken from <a href="http://vimcasts.org/blog/2013/11/registers-the-good-the-bad-and-the-ugly-parts/">this</a> website

- Good method to prevent breaking of chain for a normal mode map when instruction fails

- Option to have non literal remaps, e.g. if we have `nnoremap -o 4o`, then if you type `2-o`, you get 24 new lines, when you might have expected eight.

- Fixing all the small waits due to maps, e.g. pressing `Esc` in visual mode

- Using the up/down arrows in insert mode to move across lines does not preserve column position when passing across the end of a line

- Sometimes the position of the status bar is too high, but is corrected when you try and scroll

- <C-p> and <C-n> completion in the command line bar - especially for search and replace!

- Show all spelling errors in document in one list so one can quickly see which ones are actual errors (Edit: this has been done - http://www.vim.org/scripts/script.php?script_id=3844. Also need to install http://www.vim.org/scripts/script.php?script_id=4433 for this to work). Also a good error detection scheme for .tex files
