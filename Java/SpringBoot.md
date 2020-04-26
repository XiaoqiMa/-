##SpringBoot

为什么要用：
传统项目：整合ssh或者ssm，考虑配置文件，Jar冲突问题，整合起来繁琐
打包方式：打包成一个war放入tomcatwebaaps目录下执行

什么是SpringBoot
**SpringBoot是一个快速开发框架，能够帮助我们快速整合第三方框架（Maven依赖关系##Maven继承），完全采用注解化，简化XML配置，内置嵌入Http服务器（Tomcat，Jetty），默认嵌入Tomcat服务器，最终以Java应用程序进行执行**
SpringBoot项目中没有Web.xml
核心原理：（Maven依赖关系##Maven继承），完全注解化，Spring3.0之后采用注解方式启动SpringMVC，内置嵌入Http 服务器， Java创建tomat

微服务通讯技术 http+json（resetful） 轻量级
SpringBoot Web组件默认集成SpringMVC，SpringCloud依赖于SpringBoot实现微服务，使用SpringMVC编写微服务接口
SpringBoot + SpringCloud 实现微服务开发
SpringBoot 实现快速开发