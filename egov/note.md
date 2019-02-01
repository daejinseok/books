
#

[WARNING] File encoding has not been set, using platform encoding MS949, i.e. build is platform dependent!

```bash
pom.xml에 아래 utf-8 추가

	<properties>
		<project.build.sourceEncoding>utf-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>utf-8</project.reporting.outputEncoding>
	</properties>
```