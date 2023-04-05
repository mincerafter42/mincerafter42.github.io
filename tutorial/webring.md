---
title: How to make a webring
last_modified_at: 2023-04-05
---
## (With no JavaScript whatsoever, using Github, Jekyll, and Netlify)

<img src="/assets/goldring.gif" alt="" style="float:left"/>

[Webrings](https://en.wikipedia.org/wiki/Webring) are cool! However, I notice some webring tutorials are entirely dependent on JavaScript to make the webring function.
That's not good; JavaScript should have a fallback as gracefully as possible, and "nonfunctional" is not a graceful fallback.  
To counter this, I'm making my own webring tutorial. This is based on the framework I built for my Cuddler Webring.

For this tutorial, you need a <b>Netlify account</b> and a <b>repository for the webring</b> (which can be on Netlify itself).  
Netlify also supports GitHub, GitLab, BitBucket, and Azure DevOps for repositories.
**This tutorial assumes** your webring is hosted on a public GitHub repository and that you want users to be able to join via a pull request on the repository.
Change your code accordingly for other cases.  
**It is very helpful to be familiar with HTML.**  
It is helpful but not necessary to be familiar with [Jekyll](https://jekyllrb.com/).

Create a <b>GitHub repository</b> (it can be private so you can experiment around with stuff!).

## Files you need in the repository

### `Gemfile`
Create a file named `Gemfile` containing the following text:

    source "https://rubygems.org"
    gem 'jekyll'

This is just a mandatory file Netlify needs in order to use Jekyll.

### `.ruby-version`
Create a file named `.ruby-version` containing the following text (every file listed here is the name of the file followed by the text to put inside it)

    2.4.3

This is just another mandatory file for Netlify to use Jekyll.

### `_config.yml`
~~~yml
url: https://insert-your-url-here.invalid # replace with your webring's URL, which should end in .netlify.app (no slash afterwards)
include: [_redirects]
github_repo_url: https://insert-repository-url-here.invalid # replace with your repository's URL, which should begin with https://github.com/ and should also have no slash at the end
~~~
Another mandatory Jekyll file, but you can customize it. Make sure to replace the URLs with your webring's URL and repository.

### `_data/members.csv`

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

### `_layouts/html.html`
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

### `index.html`
    ---
    title: Insert Title Here
    layout: html
    ---
    <h1>Insert Heading Here</h1>
    <p>Insert a description of the webring here. Maybe link to an explanation of what a <a href=https://en.wikipedia.org/wiki/Webring>webring</a> is.<br>
    Perhaps link to a page explaining how to <a href="{{'/join'|relative_url}}">join the webring</a> (shown later in the tutorial)
    
    <p>If the ring is broken, please <a href={{site.github_repo_url}}/issues/new>submit an error report on GitHub</a>.
    
    <h2 id=members>Members ({{site.data.members.size}})</h2>
    <ul>
    {% for member in site.data.members %}
    <li><a href="{{member.url | xml_escape}}">{{member.name | xml_escape | newline_to_br}}</a>{% endfor %}
    </ul>

You should most certainly replace the placeholder text there.  
This HTML file has front matter, which specifies a title and that it uses the `html` layout.
Jekyll will first follow the instructions it's given between the `{%` and  `%}`, and between the `{{` and `}}`,
then apply the `html` layout to it.  
The for loop at the end of the page prints a list of all the members from `_data/members.csv`.

### `_redirects`

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

### `join.html` (if you want users to be able to join)
~~~html
---
title: How to Join
layout: html
---
<h1>Insert a relevant h1 here</h1>
<h2>Criteria to join</h2>
<ul>
<li>Insert the criteria to join the webring here.
<li>I suggest a policy on clearly marking any NSFW content (there are kids on the World Wide Web, after all. And adults at work.).
<li>and having no hate speech or bigotry.
<li>and not being advertisement-focused.
</ul>

<small>It is impossible to enumerate everything that is not allowed. For this reason, we (the webmasters) reserve the right to remove a site if we feel it is outside of our own personal bounds.</small>

<h2>Add yourself to the members list</h2>
<p>Add a unique slug, your webpage's name, and your webpage's URL to <a href={{site.github_repo_url}}/blob/main/_data/members.csv>the members list on GitHub</a> in a pull request.<br>
Pull requests can also be used to change your existing entry or delete your entry.</p>

<details>
<summary>If you don't have a GitHub account, fill out this form instead:</summary>
<form name=signup method=POST data-netlify=true netlify-honeypot=bot>
<div hidden><label>Leave this blank unless you're spam <input name=bot></label></div>
<label>Slug <input name=slug pattern=[0-9a-z](?:-?[0-9a-z])* required></label>
(ASCII lowercase letters, digits, and hyphen-minuses)<br>
<label>Name <textarea name=name></textarea></label><br>
<label>URL <input name=url type=url></label><br>
<label>E-mail address <input type=email name=email required></label><br>You'll receive an e-mail when your addition/change is made.<br>
<input type=submit>
</form>
If you're editing your existing entry, make sure to use the same slug. If you're deleting your existing entry, leave the URL field blank.
</details>

<h2>Add links on your webpage</h2>
<p>Once you're on the members list, add links on your webpage to <b>{{'/YOUR-SLUG/next'|absolute_url}}</b> and <b>{{'/YOUR-SLUG/previous'|absolute_url}}</b>, replacing <b>YOUR-SLUG</b> with the slug you chose.<br>
Feel free to include a link to <b>{{'/'|absolute_url}}</b> as well.<br>
Check if <a href=https://html.spec.whatwg.org/dev/sections.html#the-aside-element>the <code>&lt;aside&gt;</code> element</a> is right for you.
~~~
This is a page instructing users how to join.  
Users are given a link to the members list on GitHub, or, if they don't have a GitHub account,
a form to fill out. The form will automatically be collected using Netlify Forms.  
Users are then told which links to add to their webpage, and informed about the `<aside>` element,
because I think the `<aside>` element is important for webring members to know about.  
If you choose to use the form's e-mail address input, **there is no automated system to send e-mails. You'd have to send them manually.**

Of course you can change this file in any way you want, just like the others.
### `404.html` (optional)

    ---
    title: Not Found
    layout: html
    ---
    <h1>404 Not Found</h1>
    <p>If you got here by clicking a link, somebody didn't configure their part of the webring correctly, and <a href={{site.github_repo_url}}/issues/new>submitting an error report on GitHub</a> is recommended.

This page will be displayed if a user tries to access a page which doesn't exist. In that case, they'll be told to submit an error report.
If you don't include this file, users who try to access nonexistent pages will just be shown Netlify's default Not Found page.
### `main.css` (optional but recommended)
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

If your GitHub repository is still private, make sure to set it to public now.
{%endraw%}
