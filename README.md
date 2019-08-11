# pass-hole<br><br><br>

## About
A simple password manager with no special features, just a keychain app for very quickly copying and pasting from a local json file. For a relative who finds password managers too difficult to understand but also finds typing with a CLI too slow.
<br><br><br>

---

## Manager Usage

* ### add_entry(title, email, username, password)
    `title` is the title of the entry, used to refer to the entry when adding, editing or deleting. This could be the website name, including incrementors. The E-mail, username and password are self-explanatory.
    <br><br>

* ### edit_entry(title, email, username, password)
    Same as add_entry() but will throw an error if the title doesn't already exist.
    <br><br>

* ### delete_entry(title)
    Deletes the entry `title`.
    <br><br>

* ### get_entry(title)
    returns the entry `title` as a single dictionary item.
    <br><br>

* ### get_all_entries()
    returns the entire dictionary
    <br><br>
