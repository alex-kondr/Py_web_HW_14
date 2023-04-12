
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="generator" content="Docutils 0.19: https://docutils.sourceforge.io/" />

    <title>Welcome to App Contact’s documentation! &#8212; App Contacts  documentation</title>
    <link rel="stylesheet" type="text/css" href="_static/pygments.css" />
    <link rel="stylesheet" type="text/css" href="_static/nature.css" />
    <script data-url_root="./" id="documentation_options" src="_static/documentation_options.js"></script>
    <script src="_static/doctools.js"></script>
    <script src="_static/sphinx_highlight.js"></script>
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" /> 
  </head><body>
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="nav-item nav-item-0"><a href="#">App Contacts  documentation</a> &#187;</li>
        <li class="nav-item nav-item-this"><a href="">Welcome to App Contact’s documentation!</a></li> 
      </ul>
    </div>  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <section id="welcome-to-app-contact-s-documentation">
<h1>Welcome to App Contact’s documentation!<a class="headerlink" href="#welcome-to-app-contact-s-documentation" title="Permalink to this heading">¶</a></h1>
<div class="toctree-wrapper compound">
</div>
</section>
<section id="module-main">
<span id="app-contact-s-main"></span><h1>App Contact’s main<a class="headerlink" href="#module-main" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="main.add_process_time_header">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">main.</span></span><span class="sig-name descname"><span class="pre">add_process_time_header</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">request</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Request</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">call_next</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#main.add_process_time_header" title="Permalink to this definition">¶</a></dt>
<dd><p>The add_process_time_header function is a middleware function that adds the time it took to process
the request in seconds as a header called Process-Time. This can be useful for debugging purposes.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>request</strong> – Request: Get the request object</p></li>
<li><p><strong>call_next</strong> – Call the next middleware in the chain</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A response object with a header</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="main.read_root">
<span class="sig-prename descclassname"><span class="pre">main.</span></span><span class="sig-name descname"><span class="pre">read_root</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#main.read_root" title="Permalink to this definition">¶</a></dt>
<dd><p>The read_root function returns a dictionary with the key message and value Hello world!.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>A dictionary with a single key, message</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="main.startup">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">main.</span></span><span class="sig-name descname"><span class="pre">startup</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#main.startup" title="Permalink to this definition">¶</a></dt>
<dd><p>The startup function is called when the application starts up.
It’s a good place to initialize things that are needed by your app, such as databases or caches.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>A coroutine, which is a function that returns</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.database.db">
<span id="app-contact-s-database-db"></span><h1>App Contact’s database db<a class="headerlink" href="#module-src.database.db" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.database.db.get_db">
<span class="sig-prename descclassname"><span class="pre">src.database.db.</span></span><span class="sig-name descname"><span class="pre">get_db</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#src.database.db.get_db" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_db function is a context manager that returns the database session.
It also ensures that the connection to the database is closed after each request.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>A database sessionlocal object</p>
</dd>
<dt class="field-even">Doc-author<span class="colon">:</span></dt>
<dd class="field-even"><p>Trelent</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.repository.contacts">
<span id="app-contact-s-repository-contacts"></span><h1>App Contact’s repository Contacts<a class="headerlink" href="#module-src.repository.contacts" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.create_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">create_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ContactBase</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.repository.contacts.create_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The create_contact function creates a new contact in the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – ContactBase: Get the data from the request body</p></li>
<li><p><strong>user</strong> – User: Get the user id from the jwt token</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A contact object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.get_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">get_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.repository.contacts.get_contact" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The get_contact function is used to retrieve a contact from the database.</dt><dd><dl class="simple">
<dt>It takes in three parameters:</dt><dd><ul class="simple">
<li><p>contact_id: The id of the contact you want to retrieve.</p></li>
<li><p>user: The user who is requesting this information (used for authorization).</p></li>
<li><p>db: A connection to the database that will be used for querying.</p></li>
</ul>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Get the contact from the database</p></li>
<li><p><strong>user</strong> – User: Check if the user is an admin or moderator, and can therefore view all contacts</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A contact object for a given id</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.get_contact_by_fields">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">get_contact_by_fields</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">first_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">last_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">phone</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">email</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">days_before_birth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">Contact</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.repository.contacts.get_contact_by_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_contact_by_fields function is used to search for contacts by any of the following fields:
first_name, last_name, phone, email and days_before_birth. The function returns a list of all contacts that match
the given criteria.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>user</strong> – User: Ensure that the user is logged in and has access to the database</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
<li><p><strong>first_name</strong> – str: Filter the contacts by first name</p></li>
<li><p><strong>last_name</strong> – str: Filter the contacts by last name</p></li>
<li><p><strong>phone</strong> – str: Filter the contacts by phone number</p></li>
<li><p><strong>email</strong> – str: Filter the contacts by email</p></li>
<li><p><strong>days_before_birth</strong> – int: Filter the contacts by their birthday</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>All contacts that match the specified fields</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.get_contacts">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">get_contacts</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">skip</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">limit</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Contact</span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.repository.contacts.get_contacts" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_contacts function is used to retrieve a list of contacts from the database. The function takes in three
parameters: skip, limit, and user. The skip parameter is an integer that specifies how many contacts should be
skipped before retrieving the next set of contacts. The limit parameter is an integer that specifies how many
contacts should be retrieved at once (the maximum number). Finally, the user parameter represents a User object
which contains information about who made this request for contact data.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>skip</strong> – int: Skip the first n contacts in the database</p></li>
<li><p><strong>limit</strong> – int: Limit the number of contacts returned</p></li>
<li><p><strong>user</strong> – User: Check the role of the user making the request</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A list of contacts, which is a list of dictionaries</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.remove_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">remove_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.contacts.remove_contact" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The remove_contact function removes a contact from the database.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>contact_id (int): The id of the contact to be removed.
user (User): The user who is removing the contact.
db (Session): A connection to our database, used for querying and deleting contacts.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Identify the contact to be removed</p></li>
<li><p><strong>user</strong> – User: Check if the user is authorized to delete a contact</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The contact that was removed</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.update_avatar">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">update_avatar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UploadFile</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.contacts.update_avatar" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_avatar function updates the avatar of a contact. Args: contact_id (int): The id of the contact to
update. file (UploadFile): The new avatar image for the user. user (User): The current logged-in user,
used to verify that they are updating their own account and not someone else’s.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Find the contact in the database</p></li>
<li><p><strong>file</strong> – UploadFile: Upload the avatar to the database</p></li>
<li><p><strong>user</strong> – User: Check if the user is authorized to update the contact</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The updated contact</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.update_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">update_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ContactUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.contacts.update_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_contact function updates a contact in the database. Args: contact_id (int): The id of the contact to
update. body (ContactUpdate): The updated information for the specified user’s contact. user (User): The current
logged-in user, used to verify that they are updating their own data and not someone else’s.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Identify the contact to be deleted</p></li>
<li><p><strong>body</strong> – ContactUpdate: Pass the updated contact information to the function</p></li>
<li><p><strong>user</strong> – User: Get the user id from the jwt token</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The updated contact</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.contacts.update_email_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.contacts.</span></span><span class="sig-name descname"><span class="pre">update_email_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ContactEmailUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.contacts.update_email_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_email_contact function updates the email of a contact in the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Identify the contact to be updated</p></li>
<li><p><strong>body</strong> – ContactEmailUpdate: Pass the new email address to be updated</p></li>
<li><p><strong>user</strong> – User: Check if the user is authorized to update a contact</p></li>
<li><p><strong>db</strong> – Session: Pass in the database session</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The updated contact</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.repository.groups">
<span id="app-contact-s-repository-groups"></span><h1>App Contact’s repository Groups<a class="headerlink" href="#module-src.repository.groups" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.repository.groups.create_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.groups.</span></span><span class="sig-name descname"><span class="pre">create_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">GroupModel</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span></span></span><a class="headerlink" href="#src.repository.groups.create_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The create_group function creates a new group in the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – GroupModel: Create a new group</p></li>
<li><p><strong>user</strong> – User: Get the user id from the token</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A group object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.groups.get_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.groups.</span></span><span class="sig-name descname"><span class="pre">get_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">group_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.groups.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_group function takes in a group_id and a database session,
and returns the Group object with that id. If no such group exists, it returns None.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id</strong> – int: Specify the group id of the group that is being queried</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The group object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.groups.get_groups">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.groups.</span></span><span class="sig-name descname"><span class="pre">get_groups</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">skip</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">limit</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">Group</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.repository.groups.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_groups function returns a list of groups from the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>skip</strong> – int: Skip a certain number of records</p></li>
<li><p><strong>limit</strong> – int: Limit the number of groups returned</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A list of group objects</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.groups.remove_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.groups.</span></span><span class="sig-name descname"><span class="pre">remove_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">group_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.groups.remove_group" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The remove_group function removes a group from the database.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>group_id (int): The id of the group to be removed.
user (User): The user who owns the group to be removed.
db (Session): A connection to our database, used for querying and deleting groups.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id</strong> – int: Identify the group to be removed</p></li>
<li><p><strong>user</strong> – User: Get the user id of the group owner</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The group that was removed</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.groups.update_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.groups.</span></span><span class="sig-name descname"><span class="pre">update_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">group_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">GroupUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.groups.update_group" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The update_group function updates a group in the database.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>group_id (int): The id of the group to update.
body (GroupUpdate): The updated information for the specified Group object.
user (User): The User object that is making this request, used to verify ownership of this Group object.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id</strong> – int: Identify the group to be deleted</p></li>
<li><p><strong>body</strong> – GroupUpdate: Pass the name of the group to be updated</p></li>
<li><p><strong>user</strong> – User: Check if the user is authorized to delete a group</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The updated group object</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.repository.users">
<span id="app-contact-s-repository-users"></span><h1>App Contact’s repository Users<a class="headerlink" href="#module-src.repository.users" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.confirmed_email">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">confirmed_email</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.users.confirmed_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The confirmed_email function is called when a user confirms their email address.
It sets the confirmed field of the User object to True, and commits it to the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>user</strong> – User: Pass the user object to the function</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None, because it does not have a return statement</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.create_user">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">create_user</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UserModel</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">User</span></span></span><a class="headerlink" href="#src.repository.users.create_user" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The create_user function creates a new user in the database.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>body (UserModel): The UserModel object containing the data to be inserted into the database.
db (Session): The SQLAlchemy Session object used to interact with our PostgresSQL database.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – UserModel: Validate the request body</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A user object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.get_user_by_email">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">get_user_by_email</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">email</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">User</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.users.get_user_by_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_user_by_email function takes in an email and a database session,
and returns the user associated with that email. If no such user exists, it returns None.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>email</strong> – str: Pass the email address of the user to be retrieved</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The first user with the given email, or none if no such user exists</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.save_new_password">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">save_new_password</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">password_hash</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.users.save_new_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The save_new_password function takes a user object, a password hash, and the database session as arguments.
It then sets the user’s password to be equal to the new password hash.
Finally, it commits this change to the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>user</strong> – User: Get the user object from the database</p></li>
<li><p><strong>password_hash</strong> – str: Pass in the hashed password</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.update_avatar">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">update_avatar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">email</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">url</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">User</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.users.update_avatar" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_avatar function updates the avatar of a user in the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>email</strong> – str: Identify the user</p></li>
<li><p><strong>url</strong> – str: Update the avatar url of a user</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A user object, or none if the user was not found</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.update_token">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">update_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">token</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#src.repository.users.update_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_token function updates the refresh token for a user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>user</strong> – User: Get the user’s id</p></li>
<li><p><strong>token</strong> – Optional[str]: Specify that the token parameter is optional</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.repository.users.update_user">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.repository.users.</span></span><span class="sig-name descname"><span class="pre">update_user</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UserUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">User</span></span></span><a class="headerlink" href="#src.repository.users.update_user" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The update_user function updates a user in the database.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>body (UserUpdate): The updated user information.
user (User): The current version of the User object to be updated.
db (Session): A connection to the database that will be used for updating and refreshing data.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – UserUpdate: Get the data from the request body</p></li>
<li><p><strong>user</strong> – User: Get the user from the database</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A user object</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.routes.auth">
<span id="app-contact-s-router-auth"></span><h1>App Contact’s router Auth<a class="headerlink" href="#module-src.routes.auth" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.confirmed_email">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">confirmed_email</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">token</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.confirmed_email" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The confirmed_email function is used to confirm a user’s email address.</dt><dd><p>It takes in the token that was sent to the user’s email and checks if it is valid.
If it is, then we set the confirmed field of that user to True.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>token</strong> – str: Get the email and type from the token</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The message that the email has been confirmed</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.forgot_password">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">forgot_password</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">RequestEmail</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">background_tasks</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">BackgroundTasks</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">request</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Request</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.forgot_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The forgot_password function is used to send an email to the user with a link
to reset their password. The function takes in a RequestEmail object, which contains
the user’s email address. It then checks if the user exists and if they have confirmed
their account (if not, it raises an exception). If everything is okay, it sends them
an email with instructions on how to reset their password.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – RequestEmail: Get the email from the request body</p></li>
<li><p><strong>background_tasks</strong> – BackgroundTasks: Add a task to the background tasks queue</p></li>
<li><p><strong>request</strong> – Request: Get the base_url of the application</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A dict with a message</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.login">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">login</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">OAuth2PasswordRequestForm</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(OAuth2PasswordRequestForm)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.login" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The login function is used to authenticate a user.</dt><dd><p>It takes in the username and password of the user, and returns an access token if successful.
The access token can be used to make requests on behalf of that user.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – OAuth2PasswordRequestForm: Get the username and password from the request body</p></li>
<li><p><strong>db</strong> – Session: Access the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A dictionary with the access token, refresh token and bearer</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.refresh_token">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">refresh_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">credentials</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">HTTPAuthorizationCredentials</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Security(HTTPBearer)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.refresh_token" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The refresh_token function is used to refresh the access token.</dt><dd><p>The function takes in a refresh token and returns an access_token, a new refresh_token, and the type of token.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>credentials</strong> – HTTPAuthorizationCredentials: Get the access token from the request header</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A dictionary with the new access_token, refresh_token and token type</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.request_email">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">request_email</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">RequestEmail</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">background_tasks</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">BackgroundTasks</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">request</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Request</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.request_email" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The request_email function is used to send a confirmation email to the user.</dt><dd><p>The function takes in an email address and sends a confirmation link to that
address. If the user does not exist, it returns an error message.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – RequestEmail: Validate the request body</p></li>
<li><p><strong>background_tasks</strong> – BackgroundTasks: Add a task to the background tasks queue</p></li>
<li><p><strong>request</strong> – Request: Get the base_url of the application</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository functions</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A message to the user if they are already confirmed</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.reset_password">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">reset_password</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">token</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UpdatePassword</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.reset_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The reset_password function takes a token and a body as arguments.
The token is used to verify the user’s email address, while the body contains the new password.
If verification fails, an HTTP 400 error is raised. Otherwise, the function saves
the new password in database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>token</strong> – str: Get the email and type of token from the database</p></li>
<li><p><strong>body</strong> – UpdatePassword: Get the new password from the user</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A dict with a message</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.auth.singup">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.auth.</span></span><span class="sig-name descname"><span class="pre">singup</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UserModel</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">background_tasks</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">BackgroundTasks</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">request</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Request</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">dict</span></span></span><a class="headerlink" href="#src.routes.auth.singup" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The singup function creates a new user in the database.</dt><dd><p>It takes an email, username and password as input parameters.
The function returns a JSON object with the newly created user’s information.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – UserModel: Validate the data sent by the user</p></li>
<li><p><strong>background_tasks</strong> – BackgroundTasks: Add a task to the background tasks queue</p></li>
<li><p><strong>request</strong> – Request: Get the host url to send in the email</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A dictionary with the user and a message</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.routes.contacts">
<span id="app-contact-s-router-contacts"></span><h1>App Contact’s router Contacts<a class="headerlink" href="#module-src.routes.contacts" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.create_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">create_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ContactBase</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.routes.contacts.create_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The create_contact function creates a new contact in the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – ContactBase: Get the data from the request body</p></li>
<li><p><strong>current_user</strong> – User: Get the user that is currently logged-in</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A contact object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.find_contacts_by_fields">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">find_contacts_by_fields</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">first_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">last_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">phone</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">email</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">days_before_birth</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">7</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">Contact</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.routes.contacts.find_contacts_by_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>The find_contacts_by_fields function is used to find contacts by first name, last name, phone number and email.
It also allows the user to specify how many days before a contact’s birthday they want to be notified.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>first_name</strong> – str: Specify the first name of the contact to be found</p></li>
<li><p><strong>last_name</strong> – str: Find the contact by last name</p></li>
<li><p><strong>phone</strong> – str: Search for a contact by phone number</p></li>
<li><p><strong>email</strong> – str: Find a contact by email</p></li>
<li><p><strong>days_before_birth</strong> – int: Find contacts that have their birthdays in the next 7 days</p></li>
<li><p><strong>current_user</strong> – User: Get the current user</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository layer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A list of contacts</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.read_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">read_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.routes.contacts.read_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The read_contact function is used to retrieve a single contact from the database.
It takes in an integer representing the ID of the contact, and returns a Contact object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Specify the contact id</p></li>
<li><p><strong>current_user</strong> – User: Get the current user from the database</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository layer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The contact object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.read_contacts">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">read_contacts</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">skip</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">limit</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">9</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Contact</span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.routes.contacts.read_contacts" title="Permalink to this definition">¶</a></dt>
<dd><p>The read_contacts function returns a list of contacts.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>skip</strong> – int: Skip the first n contacts</p></li>
<li><p><strong>limit</strong> – int: Limit the number of contacts returned</p></li>
<li><p><strong>current_user</strong> – User: Get the current user from the token</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository layer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A list of contacts</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.remove_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">remove_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.routes.contacts.remove_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The remove_contact function removes a contact from the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Specify the contact to be deleted</p></li>
<li><p><strong>current_user</strong> – User: Get the current user from the database</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository layer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The contact that was deleted</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.update_avatar">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">update_avatar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UploadFile</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">File(PydanticUndefined)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.routes.contacts.update_avatar" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The update_avatar function updates the avatar of a contact.</dt><dd><p>The function takes in an integer representing the id of the contact to be updated,
and a file object containing information about the new avatar image.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>contact_id</strong> – int: Identify the contact to be updated</p></li>
<li><p><strong>file</strong> – UploadFile: Upload the file to the server</p></li>
<li><p><strong>current_user</strong> – User: Get the current user</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository layer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A contact object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.contacts.update_contact">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.contacts.</span></span><span class="sig-name descname"><span class="pre">update_contact</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">ContactUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">contact_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Contact</span></span></span><a class="headerlink" href="#src.routes.contacts.update_contact" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The update_contact function updates a contact in the database.</dt><dd><p>The function takes an id of the contact to update, and a ContactUpdate object containing
all fields that should be updated.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – ContactUpdate: Get the data from the request body</p></li>
<li><p><strong>contact_id</strong> – int: Specify the id of the contact to be deleted</p></li>
<li><p><strong>current_user</strong> – User: Get the current user from the database</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A contact object</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.routes.groups">
<span id="app-contact-s-router-groups"></span><h1>App Contact’s router Groups<a class="headerlink" href="#module-src.routes.groups" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.routes.groups.create_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.groups.</span></span><span class="sig-name descname"><span class="pre">create_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">GroupModel</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span></span></span><a class="headerlink" href="#src.routes.groups.create_group" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.groups.read_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.groups.</span></span><span class="sig-name descname"><span class="pre">read_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">group_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">Group</span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.routes.groups.read_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The read_group function will return a group with the given ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id</strong> – int: Get the group from the database</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
<li><p><strong>current_user</strong> – User: Check if the user is a member of the group</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A group</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.groups.read_groups">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.groups.</span></span><span class="sig-name descname"><span class="pre">read_groups</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">skip</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">limit</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">9</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Type</span><span class="p"><span class="pre">[</span></span><span class="pre">Group</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#src.routes.groups.read_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The read_groups function returns a list of groups.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>skip</strong> – int: Skip the first n groups</p></li>
<li><p><strong>limit</strong> – int: Limit the number of groups returned</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository layer</p></li>
<li><p><strong>current_user</strong> – User: Get the current user</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A list of groups</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.groups.remove_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.groups.</span></span><span class="sig-name descname"><span class="pre">remove_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">group_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span></span></span><a class="headerlink" href="#src.routes.groups.remove_group" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The remove_group function removes a group from the database.</dt><dd><p>It requires an admin or moderator to be logged in, and it takes a group_id as input.
If the user is not an admin or moderator, they will receive a 403 error code.
If there is no such group with that id, they will receive a 404 error code.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id</strong> – int: Find the group to be updated</p></li>
<li><p><strong>db</strong> – Session: Get a database session</p></li>
<li><p><strong>current_user</strong> – User: Get the user that is currently logged in</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The removed group</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.groups.update_group">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.groups.</span></span><span class="sig-name descname"><span class="pre">update_group</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">GroupUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">group_id</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Group</span></span></span><a class="headerlink" href="#src.routes.groups.update_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_group function updates a group in the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – GroupUpdate: Update the group</p></li>
<li><p><strong>group_id</strong> – int: Find the group to be deleted</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
<li><p><strong>current_user</strong> – User: Check if the user is an admin or moderator</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A group object</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.routes.user">
<span id="app-contact-s-router-users"></span><h1>App Contact’s router Users<a class="headerlink" href="#module-src.routes.user" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.routes.user.read_users_me">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.user.</span></span><span class="sig-name descname"><span class="pre">read_users_me</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">User</span></span></span><a class="headerlink" href="#src.routes.user.read_users_me" title="Permalink to this definition">¶</a></dt>
<dd><p>The read_users_me function returns the current user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>current_user</strong> – User: Pass the user object to the function</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The current_user object, which is a user instance</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.user.update_avatar_user">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.user.</span></span><span class="sig-name descname"><span class="pre">update_avatar_user</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UploadFile</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">File(PydanticUndefined)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">User</span></span></span><a class="headerlink" href="#src.routes.user.update_avatar_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_avatar_user function updates the avatar of a user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>file</strong> – UploadFile: Get the file that was uploaded by the user</p></li>
<li><p><strong>current_user</strong> – User: Get the current user from the database</p></li>
<li><p><strong>db</strong> – Session: Get the database session</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A user object</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="src.routes.user.update_profile">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.routes.user.</span></span><span class="sig-name descname"><span class="pre">update_profile</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">body</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UserUpdate</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">current_user</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">User</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_current_user)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">User</span></span></span><a class="headerlink" href="#src.routes.user.update_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The update_profile function updates the user’s profile.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>body</strong> – UserUpdate: Pass the user information to be updated</p></li>
<li><p><strong>current_user</strong> – User: Get the user that is currently logged in</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the repository</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A user object</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.services.auth">
<span id="app-contact-s-services-auth"></span><h1>App Contact’s services Auth<a class="headerlink" href="#module-src.services.auth" title="Permalink to this heading">¶</a></h1>
<dl class="py class">
<dt class="sig sig-object py" id="src.services.auth.Auth">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.services.auth.</span></span><span class="sig-name descname"><span class="pre">Auth</span></span><a class="headerlink" href="#src.services.auth.Auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py attribute">
<dt class="sig sig-object py" id="src.services.auth.Auth.ALGORITHM">
<span class="sig-name descname"><span class="pre">ALGORITHM</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'crypt'</span></em><a class="headerlink" href="#src.services.auth.Auth.ALGORITHM" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="src.services.auth.Auth.SECRET_KEY">
<span class="sig-name descname"><span class="pre">SECRET_KEY</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'secret_key'</span></em><a class="headerlink" href="#src.services.auth.Auth.SECRET_KEY" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.create_access_token">
<em class="property"><span class="pre">async</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">create_access_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">expires_delta</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.create_access_token" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The create_access_token function creates a new access token.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>data (dict): A dictionary containing the claims to be encoded in the JWT.
expires_delta (Optional[float]): An optional timedelta of seconds for the token’s expiration time.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>data</strong> – dict: Pass in the data that will be encoded into the jwt</p></li>
<li><p><strong>expires_delta</strong> – Optional[float]: Set the expiration time of the access token</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>An encoded access token</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.create_email_token">
<span class="sig-name descname"><span class="pre">create_email_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.create_email_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The create_email_token function takes a dictionary of data and returns a token.
The token is created by encoding the data with the SECRET_KEY and ALGORITHM,
and adding an iat (issued at) timestamp and exp (expiration) timestamp to it.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>data</strong> – dict: Pass in the data that will be encoded into a jwt</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A token</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.create_refresh_token">
<em class="property"><span class="pre">async</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">create_refresh_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">dict</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">expires_delta</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.create_refresh_token" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The create_refresh_token function creates a refresh token for the user.</dt><dd><dl class="simple">
<dt>Args:</dt><dd><p>data (dict): A dictionary containing the user’s id and username.
expires_delta (Optional[float]): The number of seconds until the token expires, defaults to None.</p>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>data</strong> – dict: Pass the user id to the function</p></li>
<li><p><strong>expires_delta</strong> – Optional[float]: Set the expiry time of the refresh token</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A refresh token that is encoded using the jwt library</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.decode_refresh_token">
<em class="property"><span class="pre">async</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">decode_refresh_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">refresh_token</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.decode_refresh_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The decode_refresh_token function is used to decode the refresh token. It takes in a refresh_token as an
argument and returns the email of the user who owns that token. If there is no such user, it raises an
HTTPException with status code 401 (Unauthorized) and detail &amp;quot;Could not validate credentials&amp;quot;.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>refresh_token</strong> – str: Pass in the refresh token that was sent from the client</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The email of the user who is trying to refresh their access token</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.get_current_user">
<em class="property"><span class="pre">async</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_current_user</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">token</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(OAuth2PasswordBearer)</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">db</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Session</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">Depends(get_db)</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.get_current_user" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The get_current_user function is a dependency that will be used in the</dt><dd><p>protected endpoints. It takes a token as an argument and returns the user
if it’s valid, or raises an exception otherwise.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Access the class attributes</p></li>
<li><p><strong>token</strong> – str: Get the token from the authorization header</p></li>
<li><p><strong>db</strong> – Session: Pass the database session to the function</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A user object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.get_email_type_from_token">
<em class="property"><span class="pre">async</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">get_email_type_from_token</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">token</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.get_email_type_from_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_email_type_from_token function takes a token as an argument and returns the email address
and type of user associated with that token. If the token is invalid, it raises an HTTPException.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>token</strong> – str: Decode the token</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A tuple of email and type</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.get_password_hash">
<span class="sig-name descname"><span class="pre">get_password_hash</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">password</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.get_password_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>The get_password_hash function takes a password as input and returns the hash of that password.
The hash is generated using the pwd_context object, which is an instance of Flask-Bcrypt Bcrypt class.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>password</strong> – str: Pass in the password that is to be hashed</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A password hash</p>
</dd>
</dl>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="src.services.auth.Auth.oauth2_scheme">
<span class="sig-name descname"><span class="pre">oauth2_scheme</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">&lt;fastapi.security.oauth2.OAuth2PasswordBearer</span> <span class="pre">object&gt;</span></em><a class="headerlink" href="#src.services.auth.Auth.oauth2_scheme" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="src.services.auth.Auth.pwd_context">
<span class="sig-name descname"><span class="pre">pwd_context</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">&lt;CryptContext&gt;</span></em><a class="headerlink" href="#src.services.auth.Auth.pwd_context" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="src.services.auth.Auth.r">
<span class="sig-name descname"><span class="pre">r</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">Redis&lt;ConnectionPool&lt;Connection&lt;host=localhost,port=6379,db=0&gt;&gt;&gt;</span></em><a class="headerlink" href="#src.services.auth.Auth.r" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="src.services.auth.Auth.verify_password">
<span class="sig-name descname"><span class="pre">verify_password</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">plain_password</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">hashed_password</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#src.services.auth.Auth.verify_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The verify_password function takes a plain-text password and hashed password as arguments.
It then uses the pwd_context object to verify that the plain-text password matches the hashed one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>self</strong> – Represent the instance of the class</p></li>
<li><p><strong>plain_password</strong> – str: Pass in the plain text password that is entered by the user</p></li>
<li><p><strong>hashed_password</strong> – str: Pass in the hashed password from the database</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>A boolean value of true or false</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</section>
<section id="module-src.services.email">
<span id="app-contact-s-services-email"></span><h1>App Contact’s services Email<a class="headerlink" href="#module-src.services.email" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.services.email.send_email">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.services.email.</span></span><span class="sig-name descname"><span class="pre">send_email</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">email</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">EmailStr</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">subject</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">template_name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">username</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#src.services.email.send_email" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>The send_email function sends an email to the user with a link that they can click on to verify their account.</dt><dd><dl class="simple">
<dt>The function takes in four parameters:</dt><dd><ol class="arabic simple">
<li><p>email - the user’s email address, which is used as both the recipient and subject of the message.</p></li>
<li><dl class="simple">
<dt>subject - a string containing information about what type of verification this is (e.g., verify_email).</dt><dd><p>This will be used as part of our JWT token for authentication purposes later on when we want to verify
whether or not this token was created by us and if it has been tampered with since its</p>
</dd>
</dl>
</li>
</ol>
</dd>
</dl>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>email</strong> – EmailStr: Specify the email address of the recipient</p></li>
<li><p><strong>subject</strong> – str: Set the subject of the email</p></li>
<li><p><strong>template_name</strong> – str: Specify the template to use when sending the email</p></li>
<li><p><strong>username</strong> – str: Pass the username to the template</p></li>
<li><p><strong>host</strong> – str: Pass the hostname of the server to the template</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="module-src.services.upload_avatar">
<span id="app-contact-s-services-upload-avatar"></span><h1>App Contact’s services Upload Avatar<a class="headerlink" href="#module-src.services.upload_avatar" title="Permalink to this heading">¶</a></h1>
<dl class="py function">
<dt class="sig sig-object py" id="src.services.upload_avatar.upload_avatar">
<em class="property"><span class="k"><span class="pre">async</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">src.services.upload_avatar.</span></span><span class="sig-name descname"><span class="pre">upload_avatar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">file</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">UploadFile</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#src.services.upload_avatar.upload_avatar" title="Permalink to this definition">¶</a></dt>
<dd><p>The upload_avatar function takes in a file and name, uploads the file to cloudinary,
and returns the url of that image. The function is asynchronous because it uses await.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>file</strong> – UploadFile: Get the file from the request</p></li>
<li><p><strong>name</strong> – str: Give the image a unique name</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>The url of the uploaded image</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="indices-and-tables">
<h1>Indices and tables<a class="headerlink" href="#indices-and-tables" title="Permalink to this heading">¶</a></h1>
<ul class="simple">
<li><p><a class="reference internal" href="genindex.html"><span class="std std-ref">Index</span></a></p></li>
<li><p><a class="reference internal" href="py-modindex.html"><span class="std std-ref">Module Index</span></a></p></li>
<li><p><a class="reference internal" href="search.html"><span class="std std-ref">Search Page</span></a></p></li>
</ul>
</section>


            <div class="clearer"></div>
          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <div>
    <h3><a href="#">Table of Contents</a></h3>
    <ul>
<li><a class="reference internal" href="#">Welcome to App Contact’s documentation!</a></li>
<li><a class="reference internal" href="#module-main">App Contact’s main</a><ul>
<li><a class="reference internal" href="#main.add_process_time_header"><code class="docutils literal notranslate"><span class="pre">add_process_time_header()</span></code></a></li>
<li><a class="reference internal" href="#main.read_root"><code class="docutils literal notranslate"><span class="pre">read_root()</span></code></a></li>
<li><a class="reference internal" href="#main.startup"><code class="docutils literal notranslate"><span class="pre">startup()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.database.db">App Contact’s database db</a><ul>
<li><a class="reference internal" href="#src.database.db.get_db"><code class="docutils literal notranslate"><span class="pre">get_db()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.repository.contacts">App Contact’s repository Contacts</a><ul>
<li><a class="reference internal" href="#src.repository.contacts.create_contact"><code class="docutils literal notranslate"><span class="pre">create_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.get_contact"><code class="docutils literal notranslate"><span class="pre">get_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.get_contact_by_fields"><code class="docutils literal notranslate"><span class="pre">get_contact_by_fields()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.get_contacts"><code class="docutils literal notranslate"><span class="pre">get_contacts()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.remove_contact"><code class="docutils literal notranslate"><span class="pre">remove_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.update_avatar"><code class="docutils literal notranslate"><span class="pre">update_avatar()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.update_contact"><code class="docutils literal notranslate"><span class="pre">update_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.contacts.update_email_contact"><code class="docutils literal notranslate"><span class="pre">update_email_contact()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.repository.groups">App Contact’s repository Groups</a><ul>
<li><a class="reference internal" href="#src.repository.groups.create_group"><code class="docutils literal notranslate"><span class="pre">create_group()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.groups.get_group"><code class="docutils literal notranslate"><span class="pre">get_group()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.groups.get_groups"><code class="docutils literal notranslate"><span class="pre">get_groups()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.groups.remove_group"><code class="docutils literal notranslate"><span class="pre">remove_group()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.groups.update_group"><code class="docutils literal notranslate"><span class="pre">update_group()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.repository.users">App Contact’s repository Users</a><ul>
<li><a class="reference internal" href="#src.repository.users.confirmed_email"><code class="docutils literal notranslate"><span class="pre">confirmed_email()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.users.create_user"><code class="docutils literal notranslate"><span class="pre">create_user()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.users.get_user_by_email"><code class="docutils literal notranslate"><span class="pre">get_user_by_email()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.users.save_new_password"><code class="docutils literal notranslate"><span class="pre">save_new_password()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.users.update_avatar"><code class="docutils literal notranslate"><span class="pre">update_avatar()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.users.update_token"><code class="docutils literal notranslate"><span class="pre">update_token()</span></code></a></li>
<li><a class="reference internal" href="#src.repository.users.update_user"><code class="docutils literal notranslate"><span class="pre">update_user()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.routes.auth">App Contact’s router Auth</a><ul>
<li><a class="reference internal" href="#src.routes.auth.confirmed_email"><code class="docutils literal notranslate"><span class="pre">confirmed_email()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.auth.forgot_password"><code class="docutils literal notranslate"><span class="pre">forgot_password()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.auth.login"><code class="docutils literal notranslate"><span class="pre">login()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.auth.refresh_token"><code class="docutils literal notranslate"><span class="pre">refresh_token()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.auth.request_email"><code class="docutils literal notranslate"><span class="pre">request_email()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.auth.reset_password"><code class="docutils literal notranslate"><span class="pre">reset_password()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.auth.singup"><code class="docutils literal notranslate"><span class="pre">singup()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.routes.contacts">App Contact’s router Contacts</a><ul>
<li><a class="reference internal" href="#src.routes.contacts.create_contact"><code class="docutils literal notranslate"><span class="pre">create_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.contacts.find_contacts_by_fields"><code class="docutils literal notranslate"><span class="pre">find_contacts_by_fields()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.contacts.read_contact"><code class="docutils literal notranslate"><span class="pre">read_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.contacts.read_contacts"><code class="docutils literal notranslate"><span class="pre">read_contacts()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.contacts.remove_contact"><code class="docutils literal notranslate"><span class="pre">remove_contact()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.contacts.update_avatar"><code class="docutils literal notranslate"><span class="pre">update_avatar()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.contacts.update_contact"><code class="docutils literal notranslate"><span class="pre">update_contact()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.routes.groups">App Contact’s router Groups</a><ul>
<li><a class="reference internal" href="#src.routes.groups.create_group"><code class="docutils literal notranslate"><span class="pre">create_group()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.groups.read_group"><code class="docutils literal notranslate"><span class="pre">read_group()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.groups.read_groups"><code class="docutils literal notranslate"><span class="pre">read_groups()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.groups.remove_group"><code class="docutils literal notranslate"><span class="pre">remove_group()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.groups.update_group"><code class="docutils literal notranslate"><span class="pre">update_group()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.routes.user">App Contact’s router Users</a><ul>
<li><a class="reference internal" href="#src.routes.user.read_users_me"><code class="docutils literal notranslate"><span class="pre">read_users_me()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.user.update_avatar_user"><code class="docutils literal notranslate"><span class="pre">update_avatar_user()</span></code></a></li>
<li><a class="reference internal" href="#src.routes.user.update_profile"><code class="docutils literal notranslate"><span class="pre">update_profile()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.services.auth">App Contact’s services Auth</a><ul>
<li><a class="reference internal" href="#src.services.auth.Auth"><code class="docutils literal notranslate"><span class="pre">Auth</span></code></a><ul>
<li><a class="reference internal" href="#src.services.auth.Auth.ALGORITHM"><code class="docutils literal notranslate"><span class="pre">Auth.ALGORITHM</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.SECRET_KEY"><code class="docutils literal notranslate"><span class="pre">Auth.SECRET_KEY</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.create_access_token"><code class="docutils literal notranslate"><span class="pre">Auth.create_access_token()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.create_email_token"><code class="docutils literal notranslate"><span class="pre">Auth.create_email_token()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.create_refresh_token"><code class="docutils literal notranslate"><span class="pre">Auth.create_refresh_token()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.decode_refresh_token"><code class="docutils literal notranslate"><span class="pre">Auth.decode_refresh_token()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.get_current_user"><code class="docutils literal notranslate"><span class="pre">Auth.get_current_user()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.get_email_type_from_token"><code class="docutils literal notranslate"><span class="pre">Auth.get_email_type_from_token()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.get_password_hash"><code class="docutils literal notranslate"><span class="pre">Auth.get_password_hash()</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.oauth2_scheme"><code class="docutils literal notranslate"><span class="pre">Auth.oauth2_scheme</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.pwd_context"><code class="docutils literal notranslate"><span class="pre">Auth.pwd_context</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.r"><code class="docutils literal notranslate"><span class="pre">Auth.r</span></code></a></li>
<li><a class="reference internal" href="#src.services.auth.Auth.verify_password"><code class="docutils literal notranslate"><span class="pre">Auth.verify_password()</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.services.email">App Contact’s services Email</a><ul>
<li><a class="reference internal" href="#src.services.email.send_email"><code class="docutils literal notranslate"><span class="pre">send_email()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#module-src.services.upload_avatar">App Contact’s services Upload Avatar</a><ul>
<li><a class="reference internal" href="#src.services.upload_avatar.upload_avatar"><code class="docutils literal notranslate"><span class="pre">upload_avatar()</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#indices-and-tables">Indices and tables</a></li>
</ul>

  </div>
  <div role="note" aria-label="source link">
    <h3>This Page</h3>
    <ul class="this-page-menu">
      <li><a href="_sources/index.rst.txt"
            rel="nofollow">Show Source</a></li>
    </ul>
   </div>
<div id="searchbox" style="display: none" role="search">
  <h3 id="searchlabel">Quick search</h3>
    <div class="searchformwrapper">
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" aria-labelledby="searchlabel" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"/>
      <input type="submit" value="Go" />
    </form>
    </div>
</div>
<script>document.getElementById('searchbox').style.display = "block"</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="nav-item nav-item-0"><a href="#">App Contacts  documentation</a> &#187;</li>
        <li class="nav-item nav-item-this"><a href="">Welcome to App Contact’s documentation!</a></li> 
      </ul>
    </div>
    <div class="footer" role="contentinfo">
        &#169; Copyright 2023, alex_kondr.
      Created using <a href="https://www.sphinx-doc.org/">Sphinx</a> 6.1.3.
    </div>
  </body>
</html>