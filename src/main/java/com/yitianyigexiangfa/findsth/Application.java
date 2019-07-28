package com.yitianyigexiangfa.findsth;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.Charset;

/**
 * @author Bill Lau
 * @date 2019-07-28
 */
public class Application {


    public static void main(String[] args) throws IOException {
        URL url = new URL("https://www.baidu.com");
        HttpURLConnection httpURLConnection = (HttpURLConnection)url.openConnection();
        httpURLConnection.connect();
        String responseMessage = httpURLConnection.getResponseMessage();
        System.out.println(responseMessage);
        int responseCode = httpURLConnection.getResponseCode();
        System.out.println(responseCode);
        InputStream is = httpURLConnection.getInputStream();
        StringBuffer sb=new StringBuffer();
        int length=0;
        byte[] data=new byte[1024];
        while ((length=is.read(data))!=-1){
            String s=new String(data, Charset.forName("utf-8"));
            sb.append(s);
        }
        String message=sb.toString();
        System.out.println(message);
        is.close();
        httpURLConnection.disconnect();
    }

}
