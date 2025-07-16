</head>
<body>
  <h1>Abaqus_oneInp_MultiFor</h1>

  <p>This project provides a Python script to automate the batch submission of Abaqus jobs using a <strong>single <code>.inp</code> input file</strong> and <strong>multiple <code>.for</code> user subroutines</strong>. It is ideal for testing different Fortran subroutine variations on the same model setup.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Batch Execution:</strong> Automatically creates and submits Abaqus jobs for each <code>.for</code> file found in the current directory.</li>
    <li><strong>Single Input Model:</strong> Uses one common <code>.inp</code> file for all simulations.</li>
    <li><strong>Clean Job Naming:</strong> Automatically generates safe job names based on the input and subroutine filenames.</li>
    <li><strong>Execution Monitoring:</strong> Waits for each job to complete before starting the next.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Place one <code>.inp</code> file and all your desired <code>.for</code> files in the same directory as the script.</li>
    <li>Ensure only one <code>.inp</code> file exists in the folder.</li>
    <li>Run the script using Abaqus Python:
      <pre><code>abaqus python oneInp_multiFor.py</code></pre>
    </li>
    <li>The script will:
      <ul>
        <li>Validate that exactly one <code>.inp</code> file is present</li>
        <li>Loop through all <code>.for</code> files</li>
        <li>Create and submit a job for each subroutine</li>
        <li>Wait for each job to finish before proceeding</li>
      </ul>
    </li>
  </ol>

  <h2>Requirements</h2>
  <ul>
    <li>Abaqus with Python scripting support</li>
    <li>Exactly one valid <code>.inp</code> file</li>
    <li>Multiple valid <code>.for</code> user subroutine files</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>. Feel free to use, modify, and redistribute. Credit is appreciated.</p>

  <h2>Developer Info</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> If you need help, feel free to contact me. I'm happy to guide you.</li>
  </ul>
</body>
