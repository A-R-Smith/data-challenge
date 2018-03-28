import java.io.IOException;
import java.util.Map;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

public class MyMapper extends Mapper {

    private Text word = new Text();

    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        Map<Text,LongWritable> counts = countStrings(line);
        counts.entrySet().stream().forEach(e->{
            Text k = e.getKey();
            LongWritable v = e.getValue();
            context.write(k,v);
        });

    }

    private Map<Text,LongWritable> countStrings(String s) {

            //// ALGORITHM GOES HERE
    }
}