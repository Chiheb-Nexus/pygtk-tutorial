<?xml version='1.0'?>
<!DOCTYPE xsl:stylesheet [
<!ENTITY RE "&#10;">
<!ENTITY nbsp "&#160;">
]>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>
                
	<xsl:template match="methodname">
		<xsl:call-template name="normalize-scape">
			<xsl:with-param name="string" select="text()" />
		</xsl:call-template>
	</xsl:template>
	
	<xsl:template match="methodparam">
		<xsl:if test="position() &gt; 1">
      		<xsl:text>, </xsl:text>
    	</xsl:if>
		<xsl:apply-templates />
	</xsl:template>
	
	<xsl:template match="destructorsynopsis|methodsynopsis">
		<xsl:text>\texttt{def </xsl:text>
      	<xsl:apply-templates select="methodname" />
      	<xsl:text>(</xsl:text>
      	<xsl:apply-templates select="methodparam" />
      	<xsl:text>)}&#10;&#10;</xsl:text>
	</xsl:template>
	
	<!-- 
		This won't work: verbatim environments don't allow markup
	-->
	<!--  
	<xsl:template match="parameter[@role='keyword']" mode="latex.programlisting">
		<xsl:text>\textbf{</xsl:text>
			<xsl:apply-templates />
		<xsl:text>}</xsl:text>
	</xsl:template>
	-->
	
	<!-- 
		Copied from /usr/share/dblatex/xsl/xref.xsl with a small modification
		to fix the file links (starting with 'example/'.
		Ovewriting the dblatex implementation would be nicer.
	 -->
	<xsl:template match="ulink">
		  <!-- messy sharp (#) in newtbl table cells, so escape it -->
		  <xsl:variable name="url">
		    <xsl:choose>
		    <xsl:when test="ancestor::entry">
		      <xsl:call-template name="string-replace">
		        <xsl:with-param name="string" select="@url"/>
		        <xsl:with-param name="from" select="'#'"/>
		        <xsl:with-param name="to" select="'\#'"/>
		      </xsl:call-template>
		    </xsl:when>
		    <xsl:when test="starts-with(@url, 'examples/')">
		      <xsl:text>http://learnpygtk.org/pygtktutorial/</xsl:text>
		      <xsl:value-of select="@url"/>
		    </xsl:when>
		    <xsl:otherwise>
		      <xsl:value-of select="@url"/>
		    </xsl:otherwise>
		    </xsl:choose>
		  </xsl:variable>
		
		  <xsl:choose>
		  <xsl:when test=".=''">
		    <xsl:text>\url{</xsl:text>
		    <xsl:value-of select="$url"/>
		    <xsl:text>}</xsl:text>
		  </xsl:when>
		  <xsl:otherwise>
		    <xsl:text>\href{</xsl:text>
		    <xsl:value-of select="$url"/>
		    <xsl:text>}{</xsl:text>
		    <!-- LaTeX chars are scaped. Each / except the :// is mapped to a /\- -->
		    <xsl:apply-templates mode="slash.hyphen"/>
		    <xsl:text>}</xsl:text>
		  </xsl:otherwise>
		  </xsl:choose>
		</xsl:template>
	
	
</xsl:stylesheet>
