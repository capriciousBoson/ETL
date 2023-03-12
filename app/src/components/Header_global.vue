<template>
  <header class="p-3 mb-3 border-bottom" >
    
    <div class="container" >
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none">
          <img src="https://media.licdn.com/dms/image/C4D0BAQEujqigjNnvMw/company-logo_200_200/0/1607939154711?e=2147483647&v=beta&t=Y1lgSQ3psGR6DtDz_NBslrEl2Tg489QVcfKKrCSr1y0" alt="mdo" width="37" height="37" class="bi me-2" >
        </a>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li class="nav-item"><a href="/" class="nav-link px-2 link-dark" >Timelogs</a></li>
          <li class="nav-item"><a href="/reports" class="nav-link px-2 link-dark">Reports</a></li>
          <!--<li class="nav-item"><a href="/test" class="nav-link px-2 link-dark">Test</a></li>-->
        
        </ul>

        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
          <input type="search" class="form-control" placeholder="Search..." aria-label="Search">
        </form>

        <div class="dropdown text-end">
          <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="https://upgifs.com//img/gifs/3oEjHFHaBKjH2lojSg.gif" alt="mdo" width="32" height="32" class="rounded-circle">
          </a>
          <ul class="dropdown-menu text-small" aria-labelledby="dropdownUser1" style="">
            <li><a class="dropdown-item" href="#">New project...</a></li>
            <li><a class="dropdown-item" href="#">Settings</a></li>
            <li><a class="dropdown-item" href="#">Profile</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Sign out</a></li>
          </ul>
        </div>
      </div>
    </div>
  </header>
  <div style="margin-bottom: 30px;"></div>
  </template>
  
  <script>
  export default {
    name: 'Header_global'
  };
  </script>
  