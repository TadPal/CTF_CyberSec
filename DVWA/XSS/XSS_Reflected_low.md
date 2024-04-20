# Cross-site sripting

```html
<script>
  alert("XSS");
</script>
```

## COOKIES

Open developer tools and check storage for HttpOnly parameter in cookies

```html
<script>
  alert(document.cookie);
</script>
```

# Source

```php
<?php

header ("X-XSS-Protection: 0");

// Is there any input?
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
    // Feedback for end user
    echo '<pre>Hello ' . $_GET[ 'name' ] . '</pre>';
}

?>
```
