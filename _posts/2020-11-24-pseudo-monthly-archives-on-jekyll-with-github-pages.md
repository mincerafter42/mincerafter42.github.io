---
title: Pseudo-monthly archives on Jekyll with GitHub Pages
date: 2020-11-24 13:55 -0800
tag: Programming
---
{% raw %}
If you, like me, are hosting a blog with Jekyll on GitHub Pages and want to get as close as you can to monthly archive pages, you can try what I did.  
If you do what I did on my blog:
- You *can* have a list of months somewhere on your blog, each linking to an archive page starting at that month.
- You *can't* make the archive pages separate, they are all part of the paginated archives.
- You could use years instead of months if you wanted.

The content here will assume you are generally aware of [Jekyll](https://jekyllrb.com) and its plugin limitations within GitHub Pages' implementation.

## How it works
GitHub Pages does allow the `jekyll-paginate` plugin, which generates archive pages with a fixed number of posts per page, in reverse chronological order.  
What my code does within the pagination page is place elements with IDs for each month at the beginning of each month (before the last post in the month because it's reverse chronological order).  
Outside the pagination page, I have a monthly archive document (for inclusion in other pages via the `include` tag), which lists the months, and links to the correct element in the correct archive page.

## The code
In my `_config.yml` I have `paginate_path` set to `/archive/:num`, although you could set it to something else.  
The relevant parts of my `/archive/index.html` file are
```
...
{% for post in paginator.posts %}
 {% assign this_post_month = post.date | date: site.month_format %}
 {% assign prev_post_month = post.next.date | date: site.month_format %}
 {% if this_post_month != prev_post_month %}
 <div id="{{ this_post_month }}">Month: {{ this_post_month }}</div>
 {% endif %}
 ...
{% endfor %}
...
```
Here there's a pretty expected loop looping through `paginator.posts`. The first thing every cycle of the loop does is assign the variables `this_post_month` and `next_post_month` to the dates of the current post, and the post before it in the pagination (later in time) using `site.month_format`.  
I've set `site.month_format` to "%Y-%m" (the ISO 8601 month format) but you could change it to any format that only includes the month and year.  
After setting the variables, we check if they are inequal. If they are inequal that means the current post is from a different month than the post before it (later in time). If this is the case we print an element with the post's month as its ID and content.  
The link to the post itself is printed *after* the month is printed. I also did this with years, though I don't currently plan to have a yearly archive, and I made the div element have a class to change how it looks.

Now we have the archive page set up with clear separators every month, but we still need to link to it. I have a file in my `_includes` folder to link to the monthly archives, and here is the entire file:
```
<h2>Archives</h2>
<ul>
	{% for post in site.posts %}
	{% assign this_post_month = post.date | date: site.month_format %}
	{% assign prev_post_month = post.next.date | date: site.month_format %}
	{% if this_post_month != prev_post_month %}
	{% assign archive_page = forloop.index0 | divided_by: site.paginate | plus: 1 %}
	<li>
		{% if archive_page == 1 %}
		<a href="/archive#{{ this_post_month }}">{{ this_post_month }}</a>
		{% else %}
		<a href="{{ site.paginate_path | replace: ':num', archive_page }}#{{ this_post_month }}">{{ this_post_month }}</a>
		{% endif %}
	</li>
	{% endif %}
	{% endfor %}
</ul>
```
I am formatting the monthly archives as a list with a header at the top, but you could do something else.  
I have a loop looping through `site.posts`, every post in the site in reverse chronological order.  
Similarly to the pagination page, in every cycle of the loop we check if the current post is the first in a new month. If it is, we need to set the `archive_page` variable to the correct archive page:  
We start with the `forloop.index0` variable. This gives the index, starting at 0, of the current post within the list of all posts. We then use the `divided_by` filter and divide it by `site.paginate`, the user-defined number of posts per pagination page. `divided_by` automatically rounds down when the second number is an integer, which it always is in this case. Thus, if there were 5 posts per pagination page, posts 0, 1, 2, 3, 4 would all return 0 so far. However the pages are 1-indexed, not 0-indexed, which is why we add 1.  
Next, after getting the correct archive page, we link to the element with ID in that page. The code here may be different for you since it assumes your archive path is `/archive` (in the portion if the page is page 1) so you would have to change that if it's not the case.

That's all there is! Now you too can have the same type of monthly archives that I do!
{% endraw %}
