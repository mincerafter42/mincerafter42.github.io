---
title: How to make a webring
---
## (With no JavaScript whatsoever, using Github, Jekyll, and Netlify)
![]({{'/assets/goldring.gif'|relative_url}})

[Webrings](https://en.wikipedia.org/wiki/Webring) are cool! However, I notice some webring tutorials are entirely dependent on JavaScript to make the webring function.
That's not good; JavaScript should have a fallback as gracefully as possible, and "nonfunctional" is not a graceful fallback.  
To counter this, I'm making my own webring tutorial. This is based on the framework I built for my Cuddler Webring.

<aside>
This tutorial is sadgrl approved.<br>
<q>you def should [make this tutorial] because my method is awful lmao</q> -sadgrl, 2022-05-23
</aside>

For this tutorial, you need a <b>GitHub account</b> and a <b>Netlify account</b>.
Netlify also supports GitLab, BitBucket, and Azure DevOps, so you can use one of those instead, but some URLs may need to change.  
It is helpful but not necessary to be familiar with [Jekyll](https://jekyllrb.com/).

Create a <b>GitHub repository</b> (it can be private so you can experiment around with stuff!).

## Files you need in the repository

### Gemfile

    source "https://rubygems.org"
    gem 'jekyll'

### .ruby-version

    2.4.3

These are just mandatory files Netlify needs to be able to use Jekyll.

### _config.yml
~~~yml
url: https://insert-your-url-here.invalid # replace with your webring's URL, which should end in .netlify.app (no slash afterwards)
include: [_redirects]
kramdown:
 syntax_highlighter: +nil+
 smart_quotes: "39,39,34,34"
github_repo_url: https://insert-repository-url-here.invalid # replace with your repository's URL, which should begin with https://github.com/ and should also have no slash at the end
~~~
Another mandatory Jekyll file, but you can customize it. Make sure to replace the URLs with your webring's URL and repository.  
This one makes sure to include the `_redirects` file (discussed later), and disables syntax highlighting and smart quotes.

### _data/members.csv

~~~csv
slug,name,url
member1,"Member 1's website",https://example.com/1
member2,"Member 2's page of stuff, things, and thingstuff",https://example.net/two
member3,"Member three's *amazing* website of ""><🏳️‍🌈
random text characters!",https://example.org/3andom
~~~

This file contains information about the members, which Jekyll can automatically use to generate a members list and a list of redirects.
Change the lines after the first line to your members' information, using the [comma-separated values format](https://www.rfc-editor.org/rfc/rfc4180#section-2).  
`slug` has to be unique for each member, and contain only ASCII lowercase letters, digits, and hyphen-minuses.

### _layouts/html.html
{% raw %}
~~~html
---
---
<!DOCTYPE html>
<html lang=en>
<title>{{page.title}}</title>
<meta charset=utf-8>
<link rel=stylesheet href={{'main.css'|relative_url}}>
<main>
{{content}}
</main>
<footer><nav>
<a href={{'/'|relative_url}}>Index</a><br>
<a href={{site.github_repo_url}}>View on GitHub</a>
</nav></footer>
~~~
This is mostly recognizable as HTML, with some key differences. Jekyll uses the <b>front matter</b> (those hyphen-minuses at the beginning) to indicate that it should parse the file.
Jekyll will interpret the instructions between the `{{` and `}}`, and replace them with the result.  
This is a <i>layout</i>, markup we want used more than once.  
If your webring is in a language other than English, you should update the `lang=en` accordingly.

### index.md
    ---
    title: Insert Title Here
    layout: html
    ---
    # Insert Heading Here
    Insert a description of the webring here. Maybe link to an explanation of what a [webring](https://en.wikipedia.org/wiki/Webring) is.  
    Perhaps link to a page explaining how to [join the webring]({{'/join'|relative_url}}) (shown later in the tutorial)
    
    If the ring is broken, please [submit an error report on GitHub]({{site.github_repo_url}}/issues/new).
    
    ## Members ({{site.data.members.size}}) {#members}
    {% for member in site.data.members %}
    - <a href="{{member.url | xml_escape}}" markdown=0>{{member.name | xml_escape | newline_to_br}}</a>{% endfor %}

You should most certainly replace the placeholder text there.  
This file is a [Markdown](https://daringfireball.net/projects/markdown/syntax) file. Jekyll will first follow the instructions it's given between the `{%` and  `%}`, and between the `{{` and `}}`,
then convert the file from Markdown to HTML, then apply the `html` layout to it.  
The for loop at the end of the page prints a list of all the members from `_data/members.csv`.

### _redirects

    ---
    layout: none
    ---
    {% for member in site.data.members %}
    {% if forloop.last %}
    /{{member.slug | slugify}}/next  {{site.data.members.first.url}}  302
    /{{site.data.members.first.slug | slugify}}/previous  {{member.url}}  302
    {% break %}
    {% endif %}
    /{{member.slug | slugify}}/next  {{site.data.members[forloop.index].url}}  302
    /{{site.data.members[forloop.index].slug | slugify}}/previous  {{member.url}}  302
    {% endfor %}

This file is what gives the webring its actual ring functionality. For every `slug` in `_data/members.csv`, Netlify will redirect `/slug/next` and `/slug/previous` to the next and previous `url`s.

### join.md (if you want users to be able to join)
~~~md
---
title: How to Join
layout: html
---
# Insert a relevant h1 here
## Criteria to join
- Insert the criteria to join the webring here.
- I suggest a policy on clearly marking any NSFW content.
- and having no hate speech or bigotry.
- and not being advertisement-focused.

<small>It is impossible to enumerate everything that is not allowed. For this reason, we (the webmasters) reserve the right to remove a site if we feel it is outside of our own personal bounds.</small>

## Add yourself to the members list
Add a unique slug, your webpage's name, and your webpage's URL to [the members list on GitHub]({{site.github_repo_url}}/blob/main/_data/members.csv) in a pull request.  
Pull requests can also be used to change your existing entry or delete your entry.

<details>
<summary>If you don't have a GitHub account, fill out this form instead:</summary>
<form name=signup method=POST data-netlify=true netlify-honeypot=bot>
<div hidden><label>Leave this blank unless you're spam <input name=bot></label></div>
<label>Slug <input name=slug pattern="[0-9a-z](?:-?[0-9a-z])*" required></label>
(ASCII lowercase letters, digits, and hyphen-minuses)<br>
<label>Name <textarea name=name></textarea></label><br>
<label>URL <input name=url type=url></label><br>
<input type=submit>
</form>
If you're editing your existing entry, make sure to use the same slug. If you're deleting your existing entry, leave the URL field blank.
</details>

## Add links on your webpage
Once you're on the members list, add links on your webpage to<b>{{'/YOUR-SLUG/next'|absolute_url}}</b> and <b>{{'/YOUR-SLUG/previous'|absolute_url}}</b>, replacing <b>YOUR-SLUG</b> with the slug you chose.  
Feel free to include a link to <b>{{'/'|absolute_url}}</b> as well.  
Check if [the `<aside>` element](https://html.spec.whatwg.org/dev/sections.html#the-aside-element) is right for you.
~~~
This is a page instructing users how to join.  
Users are given a link to the members list on GitHub, or, if they don't have a GitHub account,
a form to fill out. The form will automatically be collected using Netlify Forms.  
Users are then told which links to add to their webpage, and informed about the `<aside>` element,
because I think the `<aside>` element is important for webring members to know about.

Of course you can change this file in any way you want, just like the others.
### 404.md (optional)

    ---
    title: Not Found
    layout: html
    ---
    # 404 Not Found
    If you got here by clicking a link, somebody didn't configure their part of the webring correctly, and [submitting an error report on GitHub]({{site.github_repo_url}}/issues/new) is recommended.

This page will be displayed if a user tries to access a page which doesn't exist. In that case, they'll be told to submit an error report.
If you don't include this file, users who try to access nonexistent pages will just be shown Netlify's default Not Found page.
### main.css (optional but recommended)
This is a [Cascading Style Sheets](https://developer.mozilla.org/en-US/docs/Web/CSS) file, which you can use to make the webring not be
generic black serif text on a white background. Customize the CSS in any way you want! I provide no default!
## Publish the webring
[Start a new Netlify site from the repository](https://app.netlify.com/start). Make sure to set the domain to the same one you have in `_config.yml`, and make sure you have the following build settings:

Base directory
: Not Set

Build command
: bundle exec jekyll build

Publish directory
: _site

If all goes well, you should see your webring when you navigate to your domain, and each member will be able to use their links as described!

If your GitHub repository is still private, make sure to set it to public if you want users to be able to join via pull request.
{%endraw%}
