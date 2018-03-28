public class MyReducer extends Reducer<Text,LongWritable,Text,LongWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (LongWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
}
