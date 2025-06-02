Here's the fixed code that includes the permission check for `WRITE_EXTERNAL_STORAGE`:

```java
package org.schabi.newpipe;

import android.app.Dialog;
import android.app.DownloadManager;
import android.content.Context;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.preference.PreferenceManager;
import android.support.annotation.NonNull;
import android.support.v4.app.DialogFragment;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.util.Log;

import java.io.File;

public class DownloadDialog extends DialogFragment {
    private static final String TAG = DialogFragment.class.getName();
    private static final int REQUEST_WRITE_STORAGE = 123;

    public static final String TITLE = "name";
    public static final String FILE_SUFFIX_AUDIO = "file_suffix_audio";
    public static final String FILE_SUFFIX_VIDEO = "file_suffix_video";
    public static final String AUDIO_URL = "audio_url";
    public static final String VIDEO_URL = "video_url";
    private Bundle arguments;

    @NonNull
    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        arguments = getArguments();
        super.onCreateDialog(savedInstanceState);
        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        builder.setTitle(R.string.download_dialog_title)
                .setItems(R.array.download_options, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        if (ContextCompat.checkSelfPermission(getActivity(), android.Manifest.permission.WRITE_EXTERNAL_STORAGE)
                                != PackageManager.PERMISSION_GRANTED) {
                            requestPermissions(new String[]{android.Manifest.permission.WRITE_EXTERNAL_STORAGE},
                                    REQUEST_WRITE_STORAGE);
                            return;
                        }
                        startDownload(which);
                    }
                });
        return builder.create();
    }

    private void startDownload(int which) {
        Context context = getActivity();
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
        String suffix = "";
        String title = arguments.getString(TITLE);
        String url = "";
        String downloadFolder = Environment.DIRECTORY_DOWNLOADS;
        switch(which) {
            case 0:     // Video
                suffix = arguments.getString(FILE_SUFFIX_VIDEO);
                url = arguments.getString(VIDEO_URL);
                downloadFolder = Environment.DIRECTORY_MOVIES;
                break;
            case 1:
                suffix = arguments.getString(FILE_SUFFIX_AUDIO);
                url = arguments.getString(AUDIO_URL);
                downloadFolder = Environment.DIRECTORY_MUSIC;
                break;
            default:
                Log.d(TAG, "lolz");
        }
        
        String downloadPath = prefs.getString(getString(R.string.download_path_key),
                Environment.getExternalStorageDirectory().getAbsolutePath() + "/" + downloadFolder);
        final File dir = new File(downloadPath);
        if(!dir.exists()) {
            boolean mkdir = dir.mkdir();
            if(!mkdir && !dir.isDirectory()) {
                Log.e(TAG, "Cant' create directory named " + dir.toString());
            }
        }

        String saveFilePath = dir + "/" + title + suffix;
        if (App.isUsingTor()) {
            Downloader.downloadFile(getContext(), url, saveFilePath);
        } else {
            DownloadManager dm = (DownloadManager) context.getSystemService(Context.DOWNLOAD_SERVICE);
            DownloadManager.Request request = new DownloadManager.Request(
                    Uri.parse(url));
            request.setDestinationUri(Uri.fromFile(new File(saveFilePath)));
            request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
            try {
                dm.enqueue(request);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQUEST_WRITE_STORAGE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // Permission granted, retry the download
                AlertDialog dialog = (AlertDialog) getDialog();
                if (dialog != null) {
                    dialog.getButton(AlertDialog.BUTTON_POSITIVE).performClick();
                }
            }
        }
    }
}
```

The main changes include:
1. Added permission check before starting download
2. Split the download logic into a separate method `startDownload()`
3. Added permission request handling
4. Added `onRequestPermissionsResult` to handle the permission grant result
5. Added constants for permission request code

The code now properly handles runtime permissions for Android 6.0 and above.