<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html> 
<body>
  <h1>Evidenta spectacolelor de stand-up</h1>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th style="text-align:left">Titlu spectacol</th>
      <th style="text-align:left">Adresa</th>
      <th style="text-align:left">Comedianti</th>
      <th style="text-align:left">Data</th>
    </tr>
    <xsl:for-each select="evidenta_spectacolelor/spectacol">
    <tr>
      <td><xsl:value-of select="titlu_spectacol/text()"/></td>
      <td><xsl:value-of select="adresa/text()"/></td>
      <td>*
         <xsl:for-each select="participanti/comediant">
            <xsl:value-of select="."/>*
         </xsl:for-each>
      </td>
      <td><xsl:value-of select="data"/></td>
    </tr>
    </xsl:for-each>
  </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

